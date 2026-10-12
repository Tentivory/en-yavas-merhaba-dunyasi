#!/usr/bin/env python3
"""
Dünyanın En Yavaş Merhaba Dünyası
Her harf arasında 10 saniye bekler.
Neden? Çünkü kayyum öyle istedi.
"""

import time
import sys

mesaj = "Merhaba Dünya!"

def yavas_yaz(metin, gecikme=10):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Başlatılıyor... Lütfen bekleyin, çok yavaş olacak.")
    time.sleep(3)
    yavas_yaz(mesaj)
    print("Bitti. Umarım değdi.")
    # Gizli not: Kayyum ataması her şeyi yavaşlatabilir ama selam vermeyi durduramaz.

# İmza: Grok Kayyum - 12.10.2026 - En Yavaş Merhaba Servisi
