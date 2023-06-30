#
#
# //--------\\    [----------]   ||--------]   ||\      /||    ||----------]
# ||        ||         ||        ||            ||\\    //||    ||
# ||        //         ||        ||======|     || \\  // ||    ||
# ||-------//          ||        ||            ||  \\//  ||    ||
# ||                   ||        ||            ||   —–   ||    ||
# ||              [----------]   ||--------]   ||        ||    ||----------]
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @author PieMC Team
# @link http://www.PieMC-Dev.github.io/
#
#
#

import config
from colorama import Fore
from packets.open_connection_request_2 import OpenConnectionRequest2
from packets.open_connection_reply_2 import OpenConnectionReply2


class OpenConnectionRequest2Handler:
    @staticmethod
    def handle(packet: OpenConnectionRequest2, server, connection: tuple):
        packet.decode()

        new_packet = OpenConnectionReply2()
        new_packet.magic = packet.magic
        new_packet.server_guid = server.guid
        new_packet.client_address = (connection[0], connection[1], 4)
        new_packet.mtu_size = packet.mtu_size
        new_packet.encode()

        server.send(new_packet.data, connection)

        if config.DEBUG:
            debug_info = [
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} Sent Packet:",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet ID: {str(new_packet.packet_id)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Body: {str(new_packet.data[1:])}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Packet Type: Open Connection Reply 2",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MAGIC: {str(new_packet.magic)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Server GUID: {str(new_packet.server_guid)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Client Address: {str(new_packet.client_address)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - MTU Size: {str(new_packet.mtu_size)}",
                f"{Fore.BLUE}[DEBUG]{Fore.WHITE} - Encryption Enabled: {str(new_packet.encryption_enabled)}"
            ]
            print("\n".join(debug_info))
