import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# Initialize Variables
current_model_name = None

current_model_name="AI-Sweden-Models/gpt-sw3-126m"
device = "cuda:0"if torch.cuda.is_available() else "cpu"
prompt = "Träd är fina för att"

# Initialize Tokenizer & Model
def create_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(model_name)

def create_model(model_name):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()
    model.to(device)
    return model

def infer(model_name, num_samples, temperature, top_p, max_tokens, prompt):
    global tokenizer
    global model
    global current_model_name

    if model_name != current_model_name:
        new_model_name = "AI-Sweden-Models/" + model_name
        tokenizer = create_tokenizer(new_model_name)
        model = create_model(new_model_name)
        current_model_name = new_model_name


    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"].to(device)

    return_string = ""

    for i in range(num_samples):
        if num_samples > 1:
            return_string += f"---- Sample {i+1} ----\n\n"
        generated_token_ids = model.generate(
            inputs=input_ids,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=temperature,
            top_p=top_p,
        )[0]
        return_string += tokenizer.decode(generated_token_ids)

    return return_string


demo = gr.Interface(
    infer,
    [
        gr.Dropdown(
            ["gpt-sw3-126m", "gpt-sw3-356m", "gpt-sw3-1.3b", "gpt-sw3-6.7b", "gpt-sw3-6.7b-v2", "gpt-sw3-20b", "gpt-sw3-40b",
             "gpt-sw3-126m-instruct", "gpt-sw3-356m-instruct", "gpt-sw3-1.3b-instruct", "gpt-sw3-6.7b-v2-instruct", "gpt-sw3-20b-instruct"],
            value="gpt-sw3-356m",
            label="Model",
            info="Model to use for prediction. Anything larger than 1.3b seem to run out of memory on a RTX 4090. The model weights will be downloaded from the model repository if it is not already present.",
        ),
        gr.Number(value=1, label="Number of samples", info="Number of samples to generate", precision=0),
        gr.Number(value=0.6, label="Temperature", info="Temperature"),
        gr.Number(value=1, label="Top P", info="Top P. If set to < 1, only the most probable tokens with probabilities that add up to top_p or higher are kept for generation."),
        gr.Number(value=256, label="Max Tokens", info="Max Tokens", precision=0),
        gr.Textbox(value="Och där mitt på kullen, stod en livs levande dromedar.", label="Prompt", info="Prompt"),
    ],
    gr.Textbox(label="Output", lines=5, info="Generated text", show_label=False),
)

if __name__ == "__main__":
    demo.launch()

