import discord
import openai

# Setting up the API keys
#DISCORD_TOKEN =  Hiding the key
# OPENAI_API_KEY = Hiding the key

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

# Set up the discord client with the necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure that the message content intent is enabled

client = discord.Client(intents=intents)

# Function to interact with OpenAI's new Completions API
def ask_openai(prompt):
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5 Turbo model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7  # Adjusting the response creativity
        )
        return response.choices[0]['text'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == client.user:
        return

    # Bot command trigger: !askAI
    if message.content.startswith('!askAI'):
        # Extract the prompt from the user's message
        prompt = message.content[len('!askAI '):].strip()

        # Avoid processing empty prompts
        if prompt:
            # Call OpenAI to get the response
            ai_response = ask_openai(prompt)

            # Send the AI's response back to the Discord channel
            await message.channel.send(ai_response)
        else:
            await message.channel.send("Please provide a prompt after `!askAI`.")

# Run the bot
client.run(DISCORD_TOKEN)
