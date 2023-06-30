# # def string
# import database.database as database

# result = database.get_all_book("123", 1, 10)
# print(result)


# async def get_user_input():
#     loop = asyncio.get_running_loop()
#     reader = asyncio.StreamReader()
#     reader_protocol = asyncio.StreamReaderProtocol(reader)
#     await loop.connect_read_pipe(lambda: reader_protocol, sys.stdin)
#     while True:
#         key = await reader.read(1)
#         if key == b'\x1b':  # Tombol Esc
#             return 'Esc'
#         else:
#             pass


# async def back_or_quit():
#     key = await get_user_input()
#     if key == 'Esc':
#         return command.S1
