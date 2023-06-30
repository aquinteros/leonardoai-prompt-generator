from resources.utils import *

def main():

	with st.sidebar:
		st.markdown(
			"""
			# Prompt Generator
			This app generates prompts for LeonardoAI's image generation model, you can also use it for Midjourney or other AI models.

			# About LeonardoAI
			LeonardoAI is a generative AI that generates images based on given prompts, you can learn more about LeonardoAI [here](https://leonardo.ai/).

			# How to use this app
			1. Select the type of prompt you want to generate.
			2. Fill the required information.
			3. Click on the "Generate Prompt" button.
			4. Copy the generated prompt and paste it in the LeonardoAI prompt field.
			5. Copy the negative prompt and paste it in the LeonardoAI negative prompt field.
			6. Generate the image and share it with the world!

			# Got any questions?
			You can contact me via email
			"""
		)

		mention(
				label="alvaro.quinteros.a@gmail.com",
				icon="📧",
				url="mailto:alvaro.quinteros.a@gmail.com"
			)
		
		st.markdown(
			"""
			Or open an issue in the GitHub repo
			"""
		)
			
		mention(
				label="leonardoai-prompt-generator",
				icon="github",
				url="https://github.com/aquinteros/leonardoai-prompt-generator"
			)
    
	colored_header("LeonardoAI Prompt Generator", color_name='blue-70', description="Generate prompts for LeonardoAI's image generation models.")

	buy_me_a_coffee(username="aquinteros", floating=False, width=221)

	formul = st.form(key="form")

	with formul:

		keyword = st.text_input(
			"Enter a keyword to generate the prompt",
			key="keyword",
		)

		prompt_type = st.selectbox(
			"Select the type of prompt you want to generate",
			["Photorealistic", "Artistic"],
			key="prompt_type",
		)

		image_type = st.selectbox(
			"Select the type of image you want to generate",
			["Digital Illustration", "Comic Book Cover", "Photograph", "Sketch", "Pencil Drawing", "Painting", "Video Still", "GIF", "Pixel Art", "Logo", "Icon", "Emoji", "Meme", "Infographic", "Chart", "Map", "Diagram", "Flowchart", "Graph", "Poster", "Flyer", "Business Card", "Letterhead", "Certificate", "Invoice", "Resume", "CV", "Letter", "Email", "Newsletter", "Presentation", "Slide", "Report", "Essay", "Article", "Blog Post", "Book", "Novel", "Poem", "Short Story", "Script", "Screenplay", "Song", "Lyrics", "Poetry", "Comic", "Comic Strip", "Comic Book", "Manga", "Graphic Novel", "Story", "Fairy Tale", "Fable", "Legend", "Myth", "Tall Tale", "Urban Legend", "Joke", "Riddle", "Haiku", "Limerick", "Sonnet", "Ballad", "Epic", "Narrative", "Memoir", "Biography", "Autobiography", "Diary", "Journal", "Log", "Letter", "Speech", "Interview", "Conversation", "Dialogue", "Monologue", "Debate", "Essay", "Article", "Blog Post", "Book", "Novel", "Poem", "Short Story", "Script", "Screenplay", "Song", "Lyrics", "Poetry", "Comic", "Comic Strip", "Comic Book", "Manga", "Graphic Novel", "Story", "Fairy Tale", "Fable", "Legend", "Myth", "Tall Tale", "Urban Legend", "Joke", "Riddle", "Haiku", "Limerick", "Sonnet", "Ballad", "Epic", "Narrative", "Memoir", "Biography", "Autobiography", "Diary", "Journal", "Log", "Letter", "Speech", "Interview", "Conversation", "Dialogue", "Monologue", "Debate"],
			key="image_type",
		)

		art_styles = st.multiselect(
			"Select the art syles that may apply in the image",
			['Studio Ghibli', 'Anime', 'Cartoon', 'Oil Painting', 'Pencil Drawing', 'Watercolor', 'Impressionism', 'Expressionism', 'Abstract', 'Realism', 'Surrealism', 'Pop Art', 'Minimalism', 'Cubism', 'Fauvism', 'Art Nouveau', 'Renaissance', 'Baroque', 'Gothic', 'Ancient Greek', 'Ancient Egyptian', 'Ancient Roman', 'Byzantine', 'Medieval', 'Rococo', 'Neoclassicism', 'Romanticism', 'Pre-Raphaelite', 'Post-Impressionism', 'Pointillism', 'Art Deco', 'Contemporary', 'Modern', 'Futurism', 'Dadaism', 'Constructivism', 'Suprematism', 'De Stijl', 'Bauhaus', 'Conceptual', 'Performance', 'Installation', 'Land', 'Street', 'Photorealism', 'Hyperrealism', 'Digital', 'Pixel', 'Glitch', 'Vaporwave', 'Cyberpunk', 'Steampunk', 'Sci-Fi', 'Fantasy', 'Horror', 'Manga', 'Comics', 'Graffiti', 'Calligraphy', 'Typography', 'Lettering', 'Tattoo', 'Body Art', 'Fashion', 'Jewelry', 'Architecture', 'Interior', 'Industrial', 'Product', 'Furniture', 'Graphic', 'Web', 'UI', 'UX', 'Game', 'Logo', 'Icon', 'Poster', 'Packaging', 'Book', 'Magazine', 'Newspaper', 'Album', 'Movie', 'TV', 'Animation', 'Video', 'Sound', 'Music', 'Performance', 'Theater', 'Dance', 'Ceramic', 'Glass', 'Metal', 'Wood', 'Textile', 'Leather', 'Paper', 'Plastic', 'Stone', 'Concrete', 'Marble', 'Brick', 'Clay', 'Sand', 'Water', 'Fire', 'Air', 'Earth', 'Nature', 'Landscape', 'Cityscape', 'Portrait', 'Figure', 'Animal', 'Botanical', 'Food', 'Still Life', 'Abstract', 'Geometric', 'Pattern', 'Texture', 'Color', 'Black & White', 'Monochrome', 'Pastel', 'Neon', 'Retro', 'Vintage', 'Grunge', 'Glitch'],
			key="art_styles",
		)

		color_scheme = st.multiselect(
			"Select the color scheme that may apply in the image",
			['Green', 'Blue', 'Red', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Black', 'White', 'Gray', 'Beige', 'Gold', 'Silver', 'Bronze', 'Copper', 'Rainbow', 'Pastel', 'Neon', 'Retro', 'Vintage', 'Grunge', 'Glitch'],
			key="color_scheme",
		)

		temp = st.slider('Temperatura (Nivel de creatividad del modelo) (0 a 1)', 0.0, 1.0, 0.5, 0.01)

		submit = st.form_submit_button(label="Generate Prompt")

	if submit:
		input_dict = {
			"keyword": keyword,
			"prompt_type": prompt_type,
			"image_type": image_type,
			"art_styles": art_styles,
			"color_scheme": color_scheme,
			"temp": temp,
		}

		result = json.loads(generate_prompt(input_dict))

		prompt = result["prompt"]

		negative_prompt = result["negative_prompt"]

		st.markdown(
			"""
			## Prompt
			"""
		)

		st.code(prompt, language="html")

		st.markdown(
			"""
			## Negative Prompt
			"""
		)

		st.code(negative_prompt, language="html")



if __name__ == "__main__":
	main()