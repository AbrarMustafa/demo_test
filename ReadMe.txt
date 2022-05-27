 
View->Command Palette
Type ->Python->Select Interpreter
Select Python which is installed (check it with terminal command "python3 --version")
 



//-------------------------python commands---------------------------// 

source v_env/bin/activate
sudo pip3 install -r requirements.txt 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0:8000 --insecure --noreload

 
//-------------------------python commands---------------------------// 
 

 