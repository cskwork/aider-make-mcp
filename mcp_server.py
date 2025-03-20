from mcstatus import JavaServer
from mcstatus.pinger import PingResponse

class MCPServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 25565):
        self.host = host
        self.port = port
        self.server = JavaServer.lookup(f"{host}:{port}")

    async def handle_connection(self):
        """Handle incoming MCP connections"""
        print(f"MCP Server running on {self.host}:{self.port}")
        while True:
            try:
                status = self.server.status()
                return PingResponse(
                    version=status.version,
                    players=status.players,
                    description="Hello World",
                    favicon=status.favicon,
                    latency=status.latency
                )
            except Exception as e:
                print(f"Error handling connection: {e}")
                return None

if __name__ == "__main__":
    server = MCPServer()
    server.handle_connection()
