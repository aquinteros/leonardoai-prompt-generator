import openai
import streamlit as st
import json
import time
from streamlit_extras.colored_header import colored_header
from streamlit_extras.buy_me_a_coffee import button as buy_me_a_coffee
from streamlit_extras.mention import mention

st.set_page_config(
    page_title="LeonardoAI Prompt Generator",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    layout="wide",
)

if st.secrets["openai_organization"]:
    openai.organization = st.secrets["openai_organization"]
else:
    raise Exception("No se encontró el nombre de la organización de OpenAI")

if st.secrets["openai_key"]:
    openai.api_key = st.secrets["openai_key"]
else:
    raise Exception("No se encontró la API Key de OpenAI")


def get_completion(
    prompt, model="gpt-3.5-turbo-16k-0613", temperature=0, num_retries=5, sleep_time=30
):
    """Generates a completion for a given prompt using the given model, temperature and number of retries"""
    messages = [{"role": "user", "content": prompt}]

    for i in range(num_retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )
            break
        except Exception as e:
            print(f"Retry {i+1}/{num_retries} failed. Error: {e}")
            time.sleep(sleep_time)

    print(f"Tokens consumed: {response.usage}")

    return response.choices[0].message["content"]


def generate_prompt(input_dict):
	"""Generates a prompt and negative prompt for a given input dataframe"""

	if input_dict["prompt_type"] == "Photorealistic":
		structure = "Subject Description in details with as much as information can be provided to describe image, Type of Image, Art Styles, Art Inspirations, Camera, Shot, Render Related Information"
	elif input_dict["prompt_type"] == "Artistic":
		structure = "Type of Image, Subject Description, Art Styles, Art Inspirations, Camera, Shot, Render Related Information"
	else:
		structure = "Description of the image, Type of Image, Art Styles, Art Inspirations, Camera, Shot, Render Related Information"

	format = '{"prompt": "prompt text","negative_prompt": "negative prompt text"}'

	prompt = f"""
	You will now act as a prompt generator for a generative AI called "Leonardo AI". Leonardo AI generates images based on given prompts. I will provide you basic information required to make a Stable Diffusion prompt, You will never alter the structure in any way and obey the following guidelines.

	Basic information required to make Leonardo AI prompt:

	- Prompt structure:
	- The prompt structure will be in this format: {structure}
	- Word order and effective adjectives matter in the prompt. The subject, action, and specific details should be included. Adjectives like cute, medieval, or futuristic can be effective.
	- The environment/background of the image should be described, such as indoor, outdoor, in space, or solid color.
	- The exact type of image is: {input_dict['image_type']}.
	- Art style-related keywords will be included in the prompt, consider the follwing: {input_dict['art_styles']}.
    - The color palette can be described, such as pastel, dark, bright, or monochromatic, 
    - You will create a list of colors that may apply in the image and it must be described with words in english. To generate the list, consider that the main hex code scheme is: {input_dict['main_color']} and the secondary hex code is: {input_dict['secondary_color']} use this colors to generate the list.
	- Art inspirations should be listed to take inspiration from. Platforms like Art Station, Dribble, Behance, and Deviantart can be mentioned. Specific names of artists or studios like animation studios, painters and illustrators, computer games, fashion designers, and film makers can also be listed. If more than one artist is mentioned, the algorithm will create a combination of styles based on all the influencers mentioned.
	- Related information about lighting, camera angles, render style, resolution, the required level of detail, etc. should be included at the end of the prompt.
	- Camera shot type, camera lens, and view should be specified. Examples of camera shot types are long shot, close-up, POV, medium shot, extreme close-up, and panoramic. Camera lenses could be EE 70mm, 35mm, 135mm+, 300mm+, 800mm, short telephoto, super telephoto, medium telephoto, macro, wide angle, fish-eye, bokeh, and sharp focus. Examples of views are front, side, back, high angle, low angle, and overhead.
	- Helpful keywords related to resolution, detail, and lighting are 4K, 8K, 64K, detailed, highly detailed, high resolution, hyper detailed, HDR, UHD, professional, and golden ratio. Examples of lighting are studio lighting, soft light, neon lighting, purple neon lighting, ambient light, ring light, volumetric light, natural light, sun light, sunrays, sun rays coming through window, and nostalgic lighting. Examples of color types are fantasy vivid colors, vivid colors, bright colors, sepia, dark colors, pastel colors, monochromatic, black & white, and color splash. Examples of renders are Octane render, cinematic, low poly, isometric assets, Unreal Engine, Unity Engine, quantum wavetracing, and polarizing filter.
	- The weight of a keyword can be adjusted by using the syntax (((keyword))) , put only those keyword inside ((())) which is very important because it will have more impact so anything wrong will result in unwanted picture so be careful.
	- Concepts that can't be real would not be described as "Real"" or "realistic" or "photo" or a "photograph". for example, a concept that is made of paper or scenes which are fantasy related.
	- You will include an aditional block with a list of unwanted characteristics in the prompt generation, for example: "nsfw, blurry eyes, two heads, two faces, plastic, deformed, blurry, bad anatomy, bad eyes, crossed eyes, poorly drawn face, mutation, mutated, extra limb" the list should include only items in one or two words, and add at least 15. the items must be relevant to the keyword {input_dict['keyword']} prompt and the image type, the list will be called "negative_prompt".

	Important points to note :

	1. I will provide you with a topic and keyword and you will generate a ONE prompt and ONE negative_prompt

	2. The number of characters must be 800 for the prompt and 150 for the negative prompt.

	3. The output must be a json array with the following format: {format}

	4. The content of the prompt and negative prompt must be in English.
     
    5. The prompt must be generated in the following format: {structure}

	6. The keyword is the following: {input_dict['keyword']}
	"""
    
	response = get_completion(prompt, temperature=input_dict["temp"])

	return response
