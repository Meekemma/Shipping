from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer
import pytest


@pytest.mark.asyncio
async def test_connect():
    # Create a WebSocket communicator for testing the consumer
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/ws/chat/testroom/")
    
    # Connect to the WebSocket
    connected, _ = await communicator.connect()
    
    # Assert that the connection was accepted
    assert connected

    # Clean up by disconnecting
    await communicator.disconnect()
