import csv
import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import PeerChannel, PeerChat, PeerUser, Channel, Chat, User

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('session_name', api_id, api_hash)

async def save_chats_to_csv(filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Chat ID', 'Sender', 'Message', 'Date'])

        async for dialog in client.iter_dialogs():
            # Check if dialog entity is one of the supported types
            if isinstance(dialog.entity, (PeerChannel, PeerChat, PeerUser, Channel, Chat, User)):
                try:
                    # Write messages for each dialog
                    async for message in client.iter_messages(dialog.id):
                        if message.text:
                            writer.writerow([
                                dialog.id,
                                message.sender_id,
                                message.text,
                                message.date
                            ])
                        elif message.media:
                            writer.writerow([
                                dialog.id,
                                message.sender_id,
                                f"[Media: {message.media}]",
                                message.date
                            ])
                    # Print confirmation message after processing each dialog
                    print(f"Dialog '{dialog.title}' (ID: {dialog.id}) has been successfully saved.")
                except Exception as e:
                    print(f"Error processing messages for dialog {dialog.title}: {e}")
            else:
                print(f"Skipped dialog {dialog.title} - Unsupported type: {type(dialog.entity)}")

def export_chats(filename):
    """Wrapper to start the client and call the async function."""
    async def main():
        await client.start()
        await save_chats_to_csv(filename)
        print(f"All chats saved to {filename}")
    
    with client:
        client.loop.run_until_complete(main())
