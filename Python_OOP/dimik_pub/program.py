import info_from_web as ifw
import info_from_web2 as ifw2

sub_dir_name=ifw2.sub_dir_name()

for item in sub_dir_name:
    ifw.create_dir(item)
