import src.display as display
import src.database as database
import src.command as command
import src.init as init

display.display_clear()


def main():

    page = 1
    page_size = 10
    is_run = True
    stage = 0
    is_show_list = False
    search = ""

    # Inisialisasi database
    database.create_table()
    init.add_initial_data()

    while is_run:
        try:
            # mancari data untuk ditampilkan
            books, page_info = database.get_all_book(search, page, page_size)
            # clear console
            display.display_clear()
            # menampilkan visual
            output = display.show(books, page_info, is_show_list, stage)

            # core algorithm
            if stage == 0:
                if output == command.M0:
                    display.display_out()
                if output == command.M1:
                    is_show_list = True
                    continue
                if output == command.M2:
                    is_show_list = False
                    continue
                if output == command.M5:
                    stage = 1
                    continue
                if output == command.M6:
                    stage = 2
                    continue

            if stage == 1:
                err = database.insert_book(
                    [output.isbn, output.judul_buku, output.pengarang, output.penerbit, output.kota, output.tahun])
                stage = 0
                if err != None:
                    return err
                continue

            if stage == 2:
                if output == command.M4:
                    stage = 0
                    continue
                if output == command.C1:
                    page -= 1
                    continue
                if output == command.C2:
                    page += 1
                    continue
                if output == command.C3:
                    stage = 3
                    continue
                if output == command.C4:
                    page = 1
                    search = ""
                    continue

            if stage == 3:
                search = output
                page = 1
                stage = 2
                continue
        except:
            is_run = False


main()
