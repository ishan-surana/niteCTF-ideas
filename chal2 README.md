# LSB challenge
Nisha ma'am asked me to take up on making LSB challnege. Initially, as per Yogesh's suggestion, tried to look into sstv. After hours of software not working properly and ultimately Shreyansh telling me that it had been done last year, I left it.<br>
SO currently, challenge basically is a rickroll video I downloaded. I have extracted the frames of the video (190 images). Plan is to hide the true flag as lsb in either 1 random image [whose clue I can provide] or in bits of all images. I have then xored these images with a fake flag, and make them unreadable. Put all these images in a pcap file (shreyansh sugesstion). As of now, almost everything is done, just need to decide if and how to further complicate the challenge.
<br><br>

### UPDATE:-
pcap and encoder/decoder scripts uploaded. fake flag is ``nite{4lmo5t_th3re_bu+_n0t_yet!}`` and can be changed. the covered.jpg is 69.jpg with steghide and password as the above fake flag. We can do some riddle about the image number as well.<br>
Also can look into audio lsb, but then again we are sending xored frames in a pcap instead of video so scrapping that idea.
