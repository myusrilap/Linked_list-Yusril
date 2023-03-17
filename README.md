Nama: Muhamad Yusril Arjulio Prayitno

NIM: 2209116065

Penjelasan dan fungsionalitas program

  Program di atas menggunakan jenis linked list yang sederhana, yaitu singly linked list. Pada singly linked list, setiap node hanya memiliki satu pointer yang menunjuk ke node berikutnya, sehingga menghubungkan semua node dalam satu arah. Pada program di atas, setiap node hanya memiliki atribut "item" untuk menyimpan data dan "next_node" untuk menunjuk ke node berikutnya.

  Program ini merupakan program untuk mengelola sebuah daftar belanjaan. Program ini memungkinkan pengguna untuk menambah, menghapus, menampilkan daftar belanjaan, dan menampilkan riwayat operasi yang dilakukan pada daftar belanjaan.
  
Elemen Penting pada program: Class LinkedList, Class Node, Method add, Method Remove, Method Display, Method Display_History, dan fungsi main.

Berikut adalah cara kerja aplikasi:

Program dimulai dengan menampilkan menu kepada pengguna dengan lima pilihan: (1) Tambah belanjaan, (2) Hapus belanjaan, (3) Tampilkan daftar belanjaan, (4) Tampilkan history, dan (5) Keluar.

Jika pengguna memilih opsi (1) Tambah belanjaan, program akan meminta pengguna untuk memasukkan nama belanjaan yang ingin ditambahkan ke daftar belanjaan. Setelah pengguna memasukkan nama belanjaan, program akan menambahkannya ke linked list yang ada dan menampilkan pesan bahwa belanjaan telah ditambahkan ke daftar belanjaan.

Jika pengguna memilih opsi (2) Hapus belanjaan, program akan menampilkan daftar belanjaan yang ada dengan nomor urut masing-masing. Pengguna kemudian diminta untuk memasukkan nomor urut belanjaan yang ingin dihapus. Setelah pengguna memasukkan nomor urut belanjaan, program akan menghapus belanjaan tersebut dari linked list yang ada dan menampilkan pesan bahwa belanjaan telah dihapus dari daftar belanjaan.

Jika pengguna memilih opsi (3) Tampilkan daftar belanjaan, program akan menampilkan daftar belanjaan yang ada dengan nomor urut masing-masing.

Jika pengguna memilih opsi (4) Tampilkan history, program akan menampilkan riwayat semua operasi yang dilakukan pada linked list, seperti menambah atau menghapus belanjaan.

Jika pengguna memilih opsi (5) Keluar, program akan keluar dari loop dan menampilkan pesan bahwa program selesai.

Jika pengguna memasukkan opsi yang tidak valid, program akan menampilkan pesan bahwa pilihan tidak valid dan kembali ke menu.

cara kerja program

Fungsi add(item):

Fungsi ini menambahkan sebuah item ke akhir linked list. Jika linked list masih kosong, item tersebut akan menjadi elemen pertama (head) pada linked list. Jika tidak, maka fungsi akan mencari node terakhir pada linked list dengan melakukan traversal dari head sampai ke node terakhir menggunakan loop while. Setelah menemukan node terakhir, item baru akan ditambahkan sebagai node baru setelah node terakhir tersebut. Setiap kali item baru ditambahkan, operasi "add" beserta item yang ditambahkan akan dicatat ke dalam history menggunakan method append.

Fungsi remove(index):

Fungsi ini menghapus item pada index tertentu pada linked list. Pertama-tama, fungsi ini memeriksa apakah linked list kosong atau tidak. Jika kosong, fungsi akan menghasilkan pesan kesalahan dan keluar dari fungsi. Selanjutnya, fungsi memeriksa apakah argumen index yang diberikan valid atau tidak. Jika index yang diberikan kurang dari 0 atau lebih besar atau sama dengan panjang linked list, fungsi akan menghasilkan pesan kesalahan dan keluar dari fungsi.

Jika item yang ingin dihapus adalah elemen pertama, maka elemen pertama (head) akan diganti dengan node berikutnya (yang bisa jadi None jika node pertama adalah node terakhir). Jika tidak, maka fungsi akan mencari node pada index yang diinginkan dengan melakukan traversal dari head sampai node pada index yang diinginkan dengan menggunakan loop while. Setelah menemukan node pada index yang diinginkan, node tersebut akan dihapus dengan mengubah next_node pada node sebelumnya sehingga mengarah ke node setelah node yang dihapus. Setiap kali item dihapus, operasi "remove" beserta item yang dihapus akan dicatat ke dalam history menggunakan method append.

Fungsi display():

Fungsi ini menampilkan daftar belanjaan pada linked list. Jika linked list kosong, fungsi akan menampilkan pesan bahwa daftar belanjaan kosong. Jika tidak, fungsi akan melakukan traversal dari head sampai ke node terakhir dan menampilkan nomor urut dan item pada setiap node menggunakan loop while.

Fungsi display_history():

Fungsi ini menampilkan history operasi pada linked list. Jika history kosong, fungsi akan menampilkan pesan bahwa belum ada operasi yang dilakukan. Jika tidak, fungsi akan melakukan traversal pada history menggunakan loop for, dan menampilkan operasi "add" atau "remove" beserta item yang terkait pada setiap operasi.

Fungsi main():

Fungsi ini merupakan fungsi utama yang berinteraksi dengan pengguna melalui input dan output. Setiap kali pengguna memilih menu 1 atau 2, fungsi akan meminta input dari pengguna dan memanggil fungsi add() atau remove() sesuai dengan input yang diberikan. Setiap kali pengguna memilih menu 3 atau 4, fungsi akan memanggil fungsi display() atau display_history() sesuai dengan pilihan pengguna. Jika pengguna memilih menu 5, program akan keluar dari loop while dan selesai.

Output Program

<img width="185" alt="image" src="https://user-images.githubusercontent.com/126448864/225901833-eb4fe896-3a0e-46db-9bee-a152cb29614c.png">

<img width="220" alt="image" src="https://user-images.githubusercontent.com/126448864/225902042-3ac9e9dd-dd3b-442d-b11e-3c37db5c8360.png">

<img width="251" alt="image" src="https://user-images.githubusercontent.com/126448864/225902411-20056b70-ed7d-4632-a451-951cb5d27f5c.png">

<img width="152" alt="image" src="https://user-images.githubusercontent.com/126448864/225902638-caeb6bf8-0a04-4653-97bc-a22f06b55bae.png">

<img width="157" alt="image" src="https://user-images.githubusercontent.com/126448864/225902778-e3d600cb-4766-4bab-87d3-7f492234bce5.png">

<img width="203" alt="image" src="https://user-images.githubusercontent.com/126448864/225902919-90036a64-4ec7-410b-8dfb-8b63870a0175.png">

<img width="202" alt="image" src="https://user-images.githubusercontent.com/126448864/225902984-4d41539c-e3b8-4707-857b-2971c6b3f8a6.png">

<img width="205" alt="image" src="https://user-images.githubusercontent.com/126448864/225903067-981c704a-ba1b-4ad0-af31-3973ab2a7541.png">






