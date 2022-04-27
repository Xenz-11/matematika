<?php

print "
                _                            _    _  _
  /\/\    __ _ | |_   ___  _ __ ___    __ _ | |_ (_)| | __  __ _
 /    \  / _` || __| / _ \| '_ ` _ \  / _` || __|| || |/ / / _` |
/ /\/\ \| (_| || |_ |  __/| | | | | || (_| || |_ | ||   < | (_| |
\/    \/ \__,_| \__| \___||_| |_| |_| \__,_| \__||_||_|\_\ \__,_|



         ┌────────────────────┐
         │  1.Penjumlahan     │
         │  2.Pengurangan     │
         │  3.Perkalian       │
         │  4.Pembagian       │
         └────────────────────┘


Pilih Metode : ";
$xenzganz=trim(fgets(STDIN,1024));
if($xenzganz == 1) {
        echo "Masukan Nilai : ";
        $jmlh1=trim(fgets(STDIN,1024));
        echo "Di Tambah : ";
        $jmlh2=trim(fgets(STDIN,1024));
        $jmlhnya = $jmlh1+$jmlh2;
        echo "";
        echo "Hasil Dari ".$jmlh1."+".$jmlh2." Adalah : ".$jmlhnya;
        echo " ";

}
elseif($xenzganz == 2) {
        echo "Masukan Nilai : ";
        $pmgn1=trim(fgets(STDIN,1024));
        echo "Di Kurangi : ";
        $pmgn2=trim(fgets(STDIN,1024));
        $pmgnnya = $pmgn1-$pmgn2;
        echo "";
        echo "Hasil Dari ".$pmgn1."-".$pmgn2." Adalah : ".$pmgnnya;

}
elseif($xenzganz == 3) {
        echo "Masukan Nilai : ";
        $pkln1=trim(fgets(STDIN,1024));
        echo "Di Kali : ";
        $pkln2=trim(fgets(STDIN,1024));
        $pklnnya = $pkln1*$pkln2;
        echo "";
        echo "Hasil Dari ".$pkln1."×".$pkln2." Adalah : ".$pklnnya;

}
elseif($xenzganz == 4) {
        echo "Masukan Nilai : ";
        $pmbgn1=trim(fgets(STDIN,1024));
        echo "Di Bagi : ";
        $pmbgn2=trim(fgets(STDIN,1024));
        $pmbgnnya = $pmbgn1/$pmbgn2;
        echo "";
        echo "Hasil Dari ".$pmbgn1."÷".$pmbgn2." Adalah : ".$pmbgnnya;

}
?>