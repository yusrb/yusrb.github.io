while True:         # While True -----> Berfungsi Sebagai Sebuah loop tak terbatas jika kondisi nilainya selalu True

     # print berfungsi Mencetak sebuah informasi ke layar atau output
     print("                                       ")       
     print("              ...........              ")
     print("               PROJECT 1               ")
     print("              '''''''''''              ")
     print("\n =============== MENU ===============")  # \n berfungsi sebagai membuat baris baru
     print("                                       ")
     print(" 1. Energi Kinetik                     ")
     print(" 2. Tekanan")
     print(" 3. Konversi Suhu")
     print(" 4. Struktur Bumi dan Perkembangannya")
     print(" 5. Mencari C Pythagoras")
     print(" 6. Perubahan Energi Panas")
     print(" 7. Mean dan Median")
     print(" 8. Usaha Energi dan Pesawat Sederhana")
     print(" 9. Getaran Gelombang Cahaya dan Tekanan ")
     print(" 10. Mencari Percepatan")
     print(" 11. Energi Potensial Gravitasi")
     print(" 12. Persamaan Linier 1 Variebel")
     print(" 13. Mengkategorikan Sudut Segitiga dari C")
     print(" 14. Mencari Gaya dan Usaha")
     print(" 15. Menghitung Luas Permukaan dan Volume Bangun Ruang")
     print(" 16. Mencari Bilangan Ganjil dalam suatu Himpunan")
     print(" 17. Gaya Coulumb")
     print(" 18. Mencari Massa Jenis dan Kecepatan")
     print(" 19. Mencari Daya dan Energi Kinetik")
     print(" 20. Membuktikan Kebenaran Dua Linier Variebel")
     print(" 21. Rangkaian Seri dan Paralel")
     print("                             ")
     print(" 0. Keluar Dari Program")
     print("                         ")
     pilih = int(input(" Pilih Angka Menu = "))

# Soal 1
     if pilih == 1:

          print(" ======================= RUMUS =========================")
          print(" Energi Kinetik (W) = 0.5 * Massa (m) * Percepatan^2 (v)")
          print(" =======================================================")
          m = float(input(" Masukkan Massa (m) = "))
          v = float(input(" Masukkan Percepatan (v) = "))
          W = 0.5 * m * v**2
          print(f" Hasil dari Energi Kinetik dengan Massa {m} kg dan Percepatan {v} m/s adalah {W} Joule" )

          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue    # -----> Berfungsi Melanjutkan atau Melompati input selanjutnya
          elif operation == ("2"):
               print(" Akhir dari Program,Sekian Terimakasih")
               print("\n") 
               break       # ----->  Berfungsi Menghentikan Loop 
               
               

# soal 2
     elif pilih == 2:

          # Menggunakan Function (def) ----> suatu sythax yang berfungsi sebagai wadah untuk fungsi" yang nantinya dapat kita panggil
          def Tekanan_hidrostastis(p,g,h):        #  (   ) -------> Parameter berfungsi sebagai nilai yang akan dipanggil untuk suatu fungsi tertentu
               Tekanan = p * g * h
               print(f" Hasil Tekanan dari Massa Jenis Air {p} kg Percepatan Gravitasi {g} m/s dan kedalaman {h} m adalah {Tekanan} pascal") 
          def Gaya_Apung (p,g,v):
               Gaya_Apung = p * g * v 
               print(f" Hasil Gaya Apung dari Massa Jenis Fluida {p} kg Percepatan gravitasi {g} m  dan volume air {v} m adalah {Gaya_Apung} N ")      

          print(" ========= TEKANAN ==========")
          print(" 1. Tekanan Hidrostastis")
          print(" 2. Gaya Apung")
          print(" ============================")
          operator = input( " Pilih = ")
          if operator == "1":
               print(" =================================== RUMUS ===========================")
               print("  Tekanan Hidrostastis = Massa (p) * Gravitasi (g) * Kedalaman (h) " )
               print(" =====================================================================")
               p = float(input(" Masukkan Massa (p) = "))
               g = float(input(" Masukkan Percepatan Gravitasi (g) = "))
               h = float(input(" Masukkan Kedalaman (h) = "))
               Tekanan_hidrostastis(p,g,h)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break


          elif operator == "2":

               print(" ============ RUMUS ============")
               print("  Gaya Apung (F) = Massa (m) * Gravitasi (g) * Volume Fluida (v)")
               print(" ===============================")
               p = float(input(" Masukkan Massa (p) = "))
               g = float(input(" Masukkan Percepatan Gravitasi (g) = "))
               v = float(input(" Masukkan Volume Fluida (v) = "))
               Gaya_Apung(p,g,v)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break
          else :
               print(" Input yang anda masukkan invalid anda dikembalikan ke menu ")
               
          print("\n")
     elif pilih == 3:
# soal 3

          def C_ke_K (suhu_celcius):
               kelvin = suhu_celcius + 273.15
               print(f" Suhu Celcius dari {suhu_celcius} dijadikan ke Kelvin adalah {kelvin}")
          def C_ke_R (suhu_celcius):
               reamur = 4/5 * suhu_celcius
               print(f" Suhu Celcius dari {suhu_celcius} dijadikan ke Reammur adalah {reamur}")
          def C_ke_F (suhu_celcius):
               fahrenheit = suhu_celcius * 9/5 + 32
               print (f" Suhu Celcius dari {suhu_celcius} dijadikan ke Fahrenheit adalah {fahrenheit}")
          def K_ke_C (suhu_kelvin):
               Celcius = suhu_kelvin - 273.15
               print(f" Suhu Kelvin dari {suhu_kelvin} dijadikan ke Celcius adalah {Celcius}")
          def K_ke_R (suhu_kelvin):
               Reamur = (suhu_kelvin - 273) * 4/5
               print(f" Suhu Kelvin dari {suhu_kelvin} dijadikan ke Reamur adalah {Reamur}")
          def K_ke_F (suhu_kelvin):
               Fahrenheit =(suhu_kelvin * 9/5) - 459.67
               print(f" Suhu Kelvin dari {suhu_kelvin} dan dijadikan ke Fahrenheit adalah {Fahrenheit}")
          def R_ke_C (suhu_reamur):
               Celcius = 5/4 * suhu_reamur
               print(f" Suhu Reamur dari {suhu_reamur} dijadikan ke Celcius adalah {Celcius}")
          def R_ke_K (suhu_reamur):
               Kelvin = (5/4 * suhu_reamur) + 273
               print(f" Suhu Reamur dari {suhu_reamur} dijadikan ke Kelvin adalah {Kelvin}")
          def R_ke_F (suhu_reamur):
               Fahrenheit = (suhu_reamur * 9/4) + 32
               print (f" Suhu Reamur dari {suhu_reamur} dijadikan ke Fahrenheit adalah {Fahrenheit}")
          def F_ke_C (suhu_fahrenheit):
               Celcius = (suhu_fahrenheit - 32) * 5/9
               print(f" Suhu Fahrenheit dari {suhu_fahrenheit} dijadikan ke Celcius adalah {Celcius}")
          def F_ke_K (suhu_fahrenheit):
               Kelvin = (suhu_fahrenheit + 459.67) * 5/9
               print(f" Suhu Fahrenheit dari {suhu_fahrenheit} dijadikan ke Kelvin adalah {Kelvin}")
          def F_ke_R (suhu_fahrenheit):
               Reamur = 4/9 * (suhu_fahrenheit - 32)
               print(f" Suhu Fahrenheit dari {suhu_fahrenheit} dijadikan ke Reamur adalah {Reamur}")
      
          print("\n")
          print("                 ===============                ")
          print("                  KONVERSI SUHU                    ")
          print("                 ===============                 ")
          print("======================================================")
          print("                 === PILIHAN ===                      ")
          print("'''''''''''''''''''''''''''''''''''''''''''''''''''''")
          print(" 1. Celcius")
          print(" 2. Kelvin")
          print(" 3. Reamur")
          print(" 4. Fahrenheit")
          print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
          print("======================================================")
          pilihan = input(" Pilih 1,2,3,4 = ")
          
          print(" ")
          if pilihan == ("1"):
               print(" DIJADIKAN KE              ")
               print(" 1.Kelvin")
               print(" 2.Reamur")
               print(" 3.Fahrenheit")
               print("=================================================")
               pilihan = input(" pilih 1,2,3 = ")

               if pilihan == ("1"):
                    suhu_celcius = int(input(" Masukkan Suhu Celcius = "))
                    C_ke_K (suhu_celcius)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
                    
               elif pilihan == ("2"):
                    suhu_celcius = int(input(" Masukkan Suhu Celcius = "))
                    C_ke_R (suhu_celcius)
                    

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
                    
               elif pilihan == ("3"):
                    suhu_celcius = int(input(" Masukkan Suhu Celcius = "))
                    C_ke_F (suhu_celcius)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
                    
               else :
                    print("input yang anda masukkan invalid")
          elif pilihan == ("2"):
               print(" DIJADIKAN KE              ")
               print(" 1.Celcius")
               print(" 2.Reamur")
               print(" 3.Fahrenheit")
               print("=======================================")
               pilihan = input(" Pilih 1,2,3 = ")


               if pilihan == ("1"):
                    suhu_kelvin = int(input(" Masukkan suhu kelvin = "))
                    K_ke_C (suhu_kelvin)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
                    
     
               elif pilihan == ("2"):
                    suhu_kelvin = int(input(" Masukkan Suhu Kelvin = "))
                    K_ke_R (suhu_kelvin)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif pilihan == ("3"):
                    suhu_kelvin = int(input(" Masukkan Suhu Kelvin = "))
                    Fahrenheit =(suhu_kelvin * 9/5) - 459.67
                    K_ke_F (suhu_kelvin)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
               else :
                    print(" input yang anda masukkan invalid anda dikembalikan ke menu")
          
          elif pilihan == ("3"):
               print(" DIJADIKAN KE              ")
               print(" 1.Celcius")
               print(" 2.Kelvin")
               print(" 3.Fahrenheit")
               print(" ===========================")
               pilihan = input(" Pilih 1,2,3 = ")

               if pilihan == ("1"):
                    suhu_reamur = int(input(" Masukkan Suhu Reamur = "))
                    R_ke_C (suhu_kelvin)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif pilihan == ("2"):
                    suhu_reamur = int(input(" Masukkan Suhu Reamur = "))
                    R_ke_K (suhu_reamur)
                   

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif pilihan == ("3"):
                    suhu_reamur = int(input(" Masukkan Suhu Reamur = "))
                    R_ke_F (suhu_reamur)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
               else :
                    print(" input yang anda masukkan invalid anda dikembalikan ke menu")

          elif pilihan == ("4"):
               print(" DIJADIKAN KE")
               print(" 1.Celcius")
               print(" 2.Kelvin")
               print(" 3.Reamur")
               print(" ========================")
               pilihan = input(" Pilih 1,2,3 = ")

               if pilihan == ("1"):
                    suhu_fahrenheit = int(input(" Masukkan Suhu Fahrenheit = "))
                    F_ke_C (suhu_fahrenheit)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif pilihan == ("2"):
                    suhu_fahrenheit = int(input(" Masukkan Suhu Fahrenheit = "))
                    F_ke_K(suhu_fahrenheit)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif pilihan == ("3"):
                    suhu_fahrenheit = int(input(" Masukkan Suhu Fahrenheit = "))
                    F_ke_K (suhu_fahrenheit)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
               else :
                    print(" input yang anda masukkan invalid anda langsung dikembalikan ke menu")
                    print("\n")


# soal 4
     elif pilih == 4:

          print(" ====================== KATEGORI GEMPA =====================")
          pga = float(input(" Masukkan Percepatan Tanah Puncak (pga) = "))     
          if ( pga >= 0) and (pga <=2.9):
               print(" Warna = Putih")
               print(" Status = Tidak Dirasakan")
               print(" Skala BMKG = I")
               print(" Deskripsi = Tidak dirasakan dan hanya bisa dideteksi oleh alat")
               print(" ================================================================")

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif (pga >= 2.9) and (pga <= 88):
               print(" Warna = Hijau")
               print(" Status = Dirasakan")
               print( " Skala BMKG = II")
               print( " Deskripsi = Dirasakan oleh banyak orang tetapi tidak menimbulkan kerusakan")
               print(" ================================================================")

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif (pga >= 89) and (pga <= 167):
               print(" Warna = Kuning")
               print(" Status = Kerusakan Ringan")
               print(" Skala BMKG = III")
               print(" Deskripsi = Struktur bangunan mengalami kerusakan kecil,seperti retak pada dinding dan sebagian atap berjatuhan")
               print(" ================================================================")

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif (pga >= 168) and (pga <= 564):
               print(" Warna = Jingga")
               print(" Status = Kerusakan Sedang")
               print(" Skala BMKG = IV")
               print(" Deskripsi = Pada bangunan sederhana terjadi kerusakan sedang seperti roboh,kaca pecah, dan lainnya")
               print(" ================================================================")

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif (pga >=564):
               print(" Warna = Merah")
               print(" Status = Kerusakan Berat")
               print(" Skala BMKG = V")
               print(" Deskripsi = Semua bangunan mengalami kerobohan dan semua struktur bangunan rusak parah")
               print(" ================================================================")

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          else :
               print(" skala yang anda masukkan invalid anda dikembalikan ke menu")
               print("\n")
    
# soal 5
     elif pilih == 5:
          
          def c (angka1,angka2):
               sisi_miring = (angka1 **2 + angka2 **2) ** 0.5
               print(" c pada segitiga dengan rumus pythagoras adalah" , sisi_miring)

          print(" ================= RUMUS ====================")
          print(" C Pythagoras = angka1^2 + angka2^2 lalu diakarkan")
          print(" ============================================")
          angka1 = int(input(" masukkan angka1 = "))
          angka2 = int(input(" masukkan angka2 = "))
          c (angka1,angka2)
          
          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue
          elif operation == ("2"):
               print(" Akhir dari program,Sekian Terimakasih")
               print("\n")
               break

    
# soal 6
     elif pilih == 6:
          def energi_panas(m,c,tawal,takhir):
               Q = m * c * (takhir - takhir)
               print(" Perubahan energi panas dari Massa " , m , "kg" , "Kalor " , c , "kg" , "dan Perubahan Suhu" , t , "adalah" , Q)

          print(" ============================ RUMUS ================================")
          print(" Perubahan Energi Panas = Massa (m) * Kalor (c) * (Tawal Akhir - Tawal Akhir)")
          print(" ===================================================================")
          m = int(input(" Masukkan Massa = "))
          c = int(input(" Masukkan Kalor = "))
          tawal = int(input(" Masukkan Tawalawal = "))
          takhir = int(input(" Masukkan Tawakakhir = "))
          energi_panas(m,c,tawal.takhir)
          
          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue
          elif operation == ("2"):
               print(" Akhir dari program,Sekian Terimakasih")
               print("\n")
               break



     
# soal 7
     elif pilih == 7:
          def mean(jumlah_data,banyak_data):
               mean = jumlah_data / banyak_data
               print(f" Hasil mean dari Jumlah data {jumlah_data} dan Banyaknya data {banyak_data} adalah {mean}")

          def median(data):
               if hitung_data % 2 == 1:
                    median = data[hitung_data // 2]
               else :
                    median = (data[(hitung_data // 2) - 1 ] + data[hitung_data // 2]) /2
               print("Median dari data adalah = " , median)
          
          print ("============ PILIH ============")
          print(" 1.MEAN")
          print(" 2.MEDIAN")
          print("================================")
          operator = input(" Pilih =")

          if operator == ("1"):
               jumlah_data = int(input(" Masukkan Jumlah Data = "))
               banyak_data = int(input(" Masukkan Banyaknya Data = "))
               mean(jumlah_data,banyak_data)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break


          elif operator == ("2"):
               data = [5,2,8,1,7,4,3]
               data.sort ()
               hitung_data = len(data)
               print(data)
               median(data)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break
          else :
               print(" Pilihan yang anda masukkan invalid anda dikembalikan ke menu")
               
# soal 8
     elif pilih == 8:

          def energi_potensial(m,g,h):
               Ep = m * g * h
               print(f" Energi Potensial dari Massa {m} kg Gravitasi {g} g dan {h} m adalah" , Ep)
          def energi_mekanik(Ek,Ep):
               Emekanik = Ek + Ep
               print(Emekanik)
               print(f" Energi Mekanik dari Energi Kinetik {Ek} dan Energi Potensial {Ep} adalah" , Emekanik)

          print(" ================ Usaha Energi dan Pesawat Sederhana ===================")
          print(" 1.Energi Potensial")
          print(" 2.Energi Mekanik")
          print(" ========================================================================")
          operator =input("Pilih 1/2 =")

          if  operator == ("1"):
               m = float(input(" Masukkan Massa (m) = "))
               g = float(input(" masukkan Gravitasi (g) = "))
               h = float(input(" masukkan Ketinggian (h) = "))
               energi_potensial(m,g,h)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif operator == ("2"):
               Ek = float(input(" Masukkan Ek ="))
               Ep = float(input(" Masukkan Em ="))
               energi_mekanik(Ek,Ep)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break
      
# soal 9
     elif pilih == 9:
          def cepat_rambat(Pg,T):
               v = Pg / T
               print(f" Hasil Cepat rambat yang dihasilkan dari Panjang Gelombang {pg} dan Periode sebesar {T} adalah {v} ")
          def tekanan (F,A):
               p = F / A
               print(f" Hasil Tekanan dari Gaya sebesar {F} dan Luas Penampang {A} adalah {p}")
        
          print(" ==================== Getaran gelombang,Cahaya dan tekanan ================")
          print(" 1.Cepat rambat")
          print(" 2.Tekanan")
          print(" ==========================================================================")
          operator = input(" pilih 1/2 =")
        
          if operator == ("1"):
               pg = float(input(" masukkan lambada ="))
               T = float(input(" masukkan T ="))
               cepat_rambat(pg,T)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif operator == ("2"):
               F = float(input(" masukkan F ="))
               A = float(input(" masukkan A ="))
               tekanan (F,A)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break
             
          
# soal 10
     elif pilih == 10:
          def percepatanz (v , t):
               percepatan = v / t
               print(f" jadi Percepatan dari Perubahan Kecepatan {v} m/s  dan Perubahan Waktu {t} s adalah {percepatan} m/s")
        
          print(" ============= PERCEPATAN ===========")
          v = float(input(" masukkan v ="))
          t = float(input(" masukkan t ="))
          print(" ====================================")
          percepatanz (v,t)

          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue
          elif operation == ("2"):
               print(" Akhir dari program,Sekian Terimakasih")
               print("\n")
               break

# soal 11
     elif pilih == 11:
          def potensial_gravitasi (m,g,h):
               W = m * g * h
               print(f" Hasil Energi Potensial Gravitasi dari Massa {m} kg Gravitasi {g} m/s dan Ketinggian Permukaan {h} m adalah {W} joule")
          
          print(" ============ Energi Potensial Gravitasi ===========")
          print(" W = m * g * h")
          print(" ===================================================")
          m = float(input(" masukkan Massa = "))
          g = float(input(" masukkan Gravitasi = "))
          h = float(input(" masukkan Ketinggian Permukaan = "))
          W (m,g,h)

          print(" 1. kembali")
          print(" 2. berhenti")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               continue
          elif operation == ("2"):
               print(" Akhir dari Program,Sekian Terimakasih")
               break
          
# soal 12
     elif pilih == 12:
          def persamaan_linier1 (a,b):
              persamaan_linier = -a / b
              print(f" Hasil Persamaan linier (x) dari {a} dan {b} adalah {persamaan_linier}")

          print(" ================ PERSAMAAN LINIER SATU VARIEBEL ===============")
          print("   RUMUS")
          print("   Ax + B = A - xB")
          print(" ===============================================================")
          
          a = float(input(" masukkan A ="))
          b = float(input(" masukkan B ="))
          persamaan_linier1(a, b)

          print(" 1. kembali")
          print(" 2. berhenti")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               continue
          elif operation == ("2"):
               print(" Akhir dari Program,Sekian Terimakasih")
               break
         
    
# soal 13   
     elif pilih == 13:
          print(" ======== KATEGORI SUDUT DARI SUDUT C ========")
          print("   C Ke Sudut")
          print("   1. A")
          print("   2. B")
          print(" ==============================================")
          operator = input(" Pilih = ")
          
          if operator == ("1"):
               sudut = int(input(" Masukkan Sudut dari c = "))
               if (sudut == 90) :
                    print(" Sudut C ke A adalah siku siku")

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif (sudut <= 90) and ( sudut >= 0):
                    print(" Sudut dari C ke A adalah Lancip")

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif (sudut >= 90) and ( sudut <= 180):
                    print(" Sudut dari C ke A adalah Tumpul")

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

          elif operator == ("2"):
               sudut = int(input(" Masukkan Sudut dari c = "))
               if (sudut == 90) :
                    print(" Sudut C ke B adalah siku siku")

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif (sudut <= 90) and ( sudut >= 0):
                    print(" Sudut dari C ke B adalah Lancip")

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif (sudut >= 90) and ( sudut <= 180):
                    print(" Sudut dari C ke B adalah Tumpul")

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
          else :
               print(" input yang anda masukkan invalid anda dikembalikan ke menu")

          

# soal 14
     elif pilih == 14:
          def Gaya(m,a):
                   F = m * a
                   print(f" Hasil Gaya yang didapat dari Massa Benda sebesar {m} Kg dan Percepatan {a} adalah {F} Joule ")
          def Usaha(F,s):
                   P = F * s
                   print(f" Hasil Usaha dari Gaya {F} dan Usaha {s} adalah {P}")

          print(" ========== Mencari Gaya dan Usaha =========")
          print(" 1.Gaya")
          print(" 2.Usaha")
          print(" ============================================")
          operator = input( " pilih 1/2 = ")
         

          if operator == ("1"):
               
               print(" ============ RUMUS ==============")
               print("   Gaya (F) = m * a")
               print(" =================================")
               m = float(input(" masukkan Massa benda (m) ="))
               a = float(input(" masukkan Percepatan (a) ="))
               Gaya(m,a)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif operator == ("2"):
               print(" ============ RUMUS ==============")
               print("   Usaha (W) = F * s")
               print(" =================================")
               F = float(input(" Masukkan Gaya (F) = "))
               s = float(input(" Masukkan Perpindahab (s) = "))
               Usaha(F,s)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break
              
              
              

# soal 15
     elif pilih == 15:
          def Luas_Bola (r):
               luas_permukaan =  4 * (22/7 * r**2)
               print(f" Luas Permukaan Bola dari Jari jari {r} adalah {luas_permukaan}")
          def Luas_Kerucut (r,s):
               Luas_permukaan = 22/7 * r * (r + s)
               print(f" Luas Permukaan Kerucut dari Jari jari {r} dan Sisi Kerucut {s} adalah {Luas_permukaan}")
          def Luas_Prisma (La,Ls):
               Luas_permukaan = (2 * La) + Ls
               print (f" Luas Permukaan Prisma Segitiga dari Luas Alas {La} dan Luas Selimut {Ls} adalah {Luas_permukaan}")
          def Volume_Bola (r):
               Volume = 4/3 * 22/7 * r**3
               print(f" Volume Bola dari Jari jari {r} adalah {Volume}")
          def Volume_Kerucut (r,t):
               Volume = 1/3 * 22/7 * r**2 * t
               print(f" Volume Kerucut dari Jari jari {r} dan Tinggi Prisma {t} adalah {Volume}")
          def Volume_Prisma (a,t,tp):
               Volume = (1/2 * a * t) * tp
               print(f" Volume Prisma Segitiga dari Alas {a} Tinggi {t} dan Tinggi Prisma {tp} adalah {Volume}")
              

          print(" Menghitung Luas dan Volume Bangun")
          print(" ============ PILIH BANGUN ===========")
          print(" Pilih Bangun Ruang")
          print(" 1.Bola")
          print(" 2.Kerucut")
          print(" 3.Prisma Segitiga")
          print(" ======================================")
          operation = input(" Pilih 1/2/3 =")

          if operation == ("1"):
               print(" Pilih")
               print(" 1.Luas")
               print(" 2.Keliling")
               operation = input(" Pilih 1/2 = ")

               if operation == ("1"):
                    r = int(input(" Masukkan Jari jari = "))
                    Luas_Bola (r)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break

               elif operation == ("2"):
                    r = int(input(" Masukkan Jari jari = "))
                    Volume_Bola(r)

                    print(" ==============================")
                    print(" 1. kembali")
                    print(" 2. berhenti")
                    print(" ==============================")
                    operation = input(" Pilih = ")
   
                    if operation == ("1"):
                         print(" Anda Kembali ke Menu")
                         continue
                    elif operation == ("2"):
                         print(" Akhir dari program,Sekian Terimakasih")
                         print("\n")
                         break
               
          elif operation == ("2"):
                    print( "Pilih")
                    print(" 1. Luas")
                    print(" 2. Volume")
                    operation = input(" Pilih 1/2 = ")

                    if operation == ("1"):
                         r = int(input(" Masukkan Jari jari = "))
                         s = int(input(" Masukkan Sisi Kerucut = "))
                         Luas_Kerucut(r,s)

                         print(" ==============================")
                         print(" 1. kembali")
                         print(" 2. berhenti")
                         print(" ==============================")
                         operation = input(" Pilih = ")
   
                         if operation == ("1"):
                              print(" Anda Kembali ke Menu")
                              continue
                         elif operation == ("2"):
                              print(" Akhir dari program,Sekian Terimakasih")
                              print("\n")
                              break
                         elif operation == ("2"):
                              r = int(input(" Masukkan Jari jari = "))
                              t = int(input(" Masukkan Tinggi Prisma = "))
                              Volume_Kerucut(r,t)
          
          elif operation == ("3"):
                    print(" Pilih")
                    print(" 1.Luas")
                    print(" 2.Keliling")
                    operation = input(" Pilih 1/2 = ")

                    if operation == ("1"):
                         La = int(input(" Masukkan Luas Alas = "))
                         Ls = int(input(" Masukkan Luas Selimut = "))
                         Luas_Prisma(La,Ls)
                         
                         print(" ==============================")
                         print(" 1. kembali")
                         print(" 2. berhenti")
                         print(" ==============================")
                         operation = input(" Pilih = ")
   
                         if operation == ("1"):
                              print(" Anda Kembali ke Menu")
                              continue
                         elif operation == ("2"):
                              print(" Akhir dari program,Sekian Terimakasih")
                              print("\n")
                              break
                         elif operation == ("2"):
                              r = int(input(" Masukkan Jari jari = "))
                              t = int(input(" Masukkan Tinggi Prisma = "))
                              Volume_Kerucut(r,t)

                    elif operation == ("2"):
                         a = int(input(" Masukkan Alas = "))
                         t = int(input(" Masukkan Tinggi = "))
                         tp = int(input(" Masukkan Tinggi Prisma = "))
                         Volume_Prisma(a,t,tp)
                         
                         print(" ==============================")
                         print(" 1. kembali")
                         print(" 2. berhenti")
                         print(" ==============================")
                         operation = input(" Pilih = ")
   
                         if operation == ("1"):
                              print(" Anda Kembali ke Menu")
                              continue
                         elif operation == ("2"):
                              print(" Akhir dari program,Sekian Terimakasih")
                              print("\n")
                              break
                         elif operation == ("2"):
                              r = int(input(" Masukkan Jari jari = "))
                              t = int(input(" Masukkan Tinggi Prisma = "))
                              Volume_Kerucut(r,t)
               

     elif pilih == 16:
               print(" Mencari bilangan ganjil dalam suatu himpunan")
               himpunan = [2,5,3,6,7,1,6,4]
               print(" sebelum dicari bilangan ganjil = " , himpunan)
               himpunan.sort()
               ganjil = [i for i in himpunan if i % 2 != 0]
               print(" Bilangan ganjil dalam himpunan adalah" , ganjil)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

     elif pilih == 17:
          def gaya_coulumb(q1 , q2):
               F = 9 * 10**9 * (q1 + q2) / r**2
               print(f" Hasil Gaya Coulumb dari Muatan1 {q1} dan Muatan2 {2} adalah {F}")

          print(" Gaya Coulumb")
          print(" Rumus = 9 * 10^9 * (q1 + q2) / r^2")
          q1 = float(input(" Masukkan Muatan1 = "))
          q2 = float(input(" Masukkan Muatan2 = "))
          gaya_coulumb(q1 , q2)

          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue
          elif operation == ("2"):
               print(" Akhir dari program,Sekian Terimakasih")
               print("\n")
               break
          elif operation == ("2"):
               r = int(input(" Masukkan Jari jari = "))
               t = int(input(" Masukkan Tinggi Prisma = "))
               Volume_Kerucut(r,t)
# Soal 18
     elif pilih == 18:
          def Massa_Jenis (m,v):
               P = m /v
               print (f" Hasil Massa Jenis dari Massa {m} dan Volume {v} adalah {P}")
          def kecepatan(s,t):
               v = s/t
               print (f" Hasil Kecepatan dari Jarak {s} m dan waktu {t} s adalah {v}")
          print(" 1. Massa Jenis ")
          print(" 2. Kecepatan ")
          operator = input(" Pilih = ")
          if operator == ("1"):
               print(" Massa Jenis = Massa (m) / Volume (v)")
               m = float(input(" Masukkan Massa (m) = "))
               v = float(input(" Masukkan Volume (v) = "))
               Massa_Jenis (m,v)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif operation == ("2"):
               r = int(input(" Masukkan Jari jari = "))
               t = int(input(" Masukkan Tinggi Prisma = "))
               Volume_Kerucut(r,t)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif operator == ("2"):
               print(" Kecepatan = Jarak (s) / Waktu (t)")
               s = float(input(" Masukkan Jarak (s) = "))
               t = float(input(" Masukkan Waktu (t) = "))
               kecepatan(s,t)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          else :
               print(" input yang anda masukkan invalid anda dikembalikan ke menu")
# Soal 19
     elif pilih == 19:
          def daya (W,t):
               P = W / t
               print(f"Hasil Dari dari Usaha {W} joule dan Waktu (t) s adalah {P} W ")
          def energi_kinetik (m,v):
               Ek = 0.5 * m * v**2
               print(f" Hasil Energi Kinetik dari Massa {m} kg dan Kecepatan {v} m/s adalah {Ek} joule ")

          print(" Pilih")
          print(' 1. Daya')
          print(" 2. Energi Kinetik")
          operator = input(" Pilih = ")
          if operator == ("1"):
               print(" Daya (P) = Usaha (W) / Waktu (t)")
               W = float(input(" Masukkan Usaha (W) = "))
               t = float(input(" Masukkan Waktu (t) = "))
               daya (W,t)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          elif operator == ("2"):
               print(" Energi Kinetik (Ek) = 0.5 * Massa (m) * Kecepatan (v)")
               m = float(input(" Masukkan Massa (m) = "))
               v = float(input(" Masukkan Kecepatan (v) = "))
               energi_kinetik (m,v)

               print(" ==============================")
               print(" 1. kembali")
               print(" 2. berhenti")
               print(" ==============================")
               operation = input(" Pilih = ")
   
               if operation == ("1"):
                    print(" Anda Kembali ke Menu")
                    continue
               elif operation == ("2"):
                    print(" Akhir dari program,Sekian Terimakasih")
                    print("\n")
                    break

          else :
               print (" Input yang anda masukkan invalid anda dikembalikan ke menu ")
# Soal 20
     elif pilih == 20:
          def kebenaran(a,b,x,y):
               kebenaran_dua_linier = a*x + b*x == y
               print(f" Kebenaran dua linier dari {a} dan {b} merupakan y {kebenaran_dua_linier}")
          print(" ================ MENCARI KEBENARAN DI DUA LINIER VARIEBEL =======================")
          print(" Kebenaran Dua Linier = (a.x) + (b.x) == y ")
          print(" =================================================================================")
          a = float(input(" Masukkan Angka1 = "))
          b = float(input(" Masukkan Angka2 = "))
          x = float(input(" Masukkan x = "))
          y = float(input(" Masukkan y = "))
          kebenaran (a,b,x,y)

          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue
          elif operation == ("2"):
               print(" Akhir dari program,Sekian Terimakasih")
               print("\n")
               break

# soal 21
     elif pilih == 21:
          def hitung_rp(resistor):
            rtotal = 0
            for R in resistor:
                rtotal += 1 / R
            print("resistor total rangkaian seri adalah = ",rtotal,"ohm")
        
          def hitung_rs(resistor):
            rtotal = 0
            for R in resistor:
                rtotal +=  R
            print("resistor total rangkaian pararel adalah = ",rtotal,"ohm")
        
          r = int(input("masukkan jumlah resistor = "))
          resistor =[]
          for i in range(r):
               nilai_r = int(input("Masukkan nilai resistor ke-" + str(i + 1) + "(ohm): "))
               resistor.append(nilai_r)
        
          hitung_rp(resistor)
          hitung_rs(resistor)

          print(" ==============================")
          print(" 1. kembali")
          print(" 2. berhenti")
          print(" ==============================")
          operation = input(" Pilih = ")
   
          if operation == ("1"):
               print(" Anda Kembali ke Menu")
               continue
          elif operation == ("2"):
               print(" Akhir dari program,Sekian Terimakasih")
               print("\n")
               break

     elif pilih == 0:
          print(" Anda Keluar dari Program")
          break



     












                    



           



            
         
         


       



         

        
                 


              

              

              
              

              
            

