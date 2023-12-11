+ files to be provide are `files.pcap` and `audio.wav`
+ The fake flag `nite{4lmo5t_th3re_bu+_n0t_yet!}` is hidden in the **audio.mp3** file with passsword `password`.
+ ``frame_splitter.py`` splits video into frames. images were put in in "source" folder.<br>
+ each frame is now put in a pcap file `files.pcap` after xoring using `encrypter.py` with fake flag.<br>
+ `decrypter.py` unxors and gets the original images in "reformed" folder.<br>
+ one of the images will be lsb'd using steghide and password will be the fakeflag. currently that image is "41.jpg" and flag.txt can be extracted. (41 because NGGYU release date 27/07/1987 => 2+7+0+7+1+9+8+7 = 41).
+ flag.txt will give real flag, currently set as `nite{real_flag}`
