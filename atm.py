restart = 'Y'
chances = 3
balance = 1000000

while chances >= 0:
    pin = int(input('Masukan 6 digit PIN anda: '))
    if pin == 201520:
        print('PIN yang anda masukan benar\n')
        while restart in ('y', 'Y', 'ya', 'YA'):
            print('Tekan 1 untuk cek saldo\n')
            print('Tekan 2 untuk tarik tunai\n')
            print('Tekan 3 untuk pembayaran\n')
            print('Tekan 4 untuk mengeluarkan kartu\n')
            option = int(input('pilih nomor: '))
            
            if option == 1:
                print('Saldo anda Rp', balance, '\n')
                restart = input('Apakah anda ingin kembali? ')
                if restart in ('n', 'N', 'no', 'NO'):
                    print('Thank You')
                break
                
            elif option == 2:
                option2 = 'y'
                withdrawl = float(
                    input(
                        'Berapa banyak anda ingin menarik uang? \nRp50.000/Rp100.000/Rp200.000/Rp500.000/Rp1.000.000 for other enter 1: ')
                    )
                if withdrawl in [50000, 100000, 200000, 500000, 1000000]:
                    balance = balance - withdrawl
                    print('\n Saldomu sekarang tersisa Rp', balance)
                    restart = input('Apakah anda ingin kembali? ')
                    if restart in ('n', 'N', 'no', 'NO'):
                        print('THANK YOU')
                        break

                elif withdrawl != [50000, 100000, 200000, 500000, 1000000]:
                    print('Jumlah penarikan tidak valid, mohon ulangi \n')
                    restart = 'y'

                elif withdrawl == 1:
                    withdrawl = float(
                        input('Silahkan masukan jumlah yang diinginkan'))

            elif option == 3:
                Pay_in = float(input('Berapa banyak kamu ingin membayar? '))
                balance = balance + Pay_in
                print('\nSaldomu sekarang Rp', balance)
                restart = input('Apakah anda ingin kembali? ')
                if restart in ('n', 'N', 'no', 'NO'):
                    print('THANK YOU')
                    break
            
            elif option == 4:
                print('Mohon tunggu sebentar, kartu anda akan di keluarkan...\n')
                print('THANK YOU')
                break
        
            else:
                print('Mohon masukan angka yang benar. \n')
                restart = 'y'

    elif pin != '201520':
        print('PIN yang anda masukan salah')
        chancesn = chances - 1
        if chances == 0:
            print('\n kesempatan habis')
        break    
                

