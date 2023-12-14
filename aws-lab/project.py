#Importing the libraries.
import discord
import os 
from ec2_metadata import ec2_metadata
import random
from dotenv import load_dotenv

#Load enviorment variable from a file.
load_dotenv()

#Initialize the Discord bot.
#Inserting the token for OAuth2.

client = discord.Client()
token = os.getenv('TOKEN')

#When bot is connected to the discord it will give a meassage saying it's "logged in as a bot(user)".
@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))

#Trigger the events if client sends a message in the server.
@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	print(f'Message {user_message} by {username} on {channel}') 

	#Nullify any messages sent from the bot itself, to avoid respoding to itself.
	if message.author == client.user: 
		return
	try:
		if channel == "random": 
			if user_message.lower() == "hello" or user_message.lower() == "hi": 
				await message.channel.send(f'Hello {username}') 
				return
			
			#Nested if conditon to output "bye" if the user inputs "bye".
			elif user_message.lower() == "bye":
				try:
					await message.channel.send(f'Bye {username}') 
					return
				except discord.errors.HTTExcution as e:
					print(f'Message failed to send due to the following:{e}')
			
			#Nested if condition to output 'hello' if the user inputs"hello world".
			elif user_message.lower() == "hello world":
				try: 
					await message.channel.send(f'hello') 
					return
				except discord.errors.HTTExcution as e:
					print(f'Message failed to send due to the following:{e}')
					
			#Nested if codition to output my ec2 data if asked "tell me about my server!".
			elif user_message.lower() == "tell me about my server!":
				try:
					await message.channel.send(f'region: {ec2_metadata.region}\nIp Address: {ec2_metadata.public_ipv4}\nAvailabilty zone: {ec2_metadata.availability_zone}\nInstance: {ec2_metadata.instance_type}')
					return
				except discord.errors.HTTExcution as e:
					print(f'Message failed to send due to the following:{e}')

	except Exception as error:
		print(f"An error occured: {error}")
			
#Execute the token by passing the token object.			 
client.run(token)

 

