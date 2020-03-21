from flask import Flask, request, render_template,jsonify
app = Flask(__name__)
def do_something(first_name,second_name):
	f="flames";
	d={'f':"FRIENDSHIP",'l':"LOVE",'a':"AFFECTION",'m':"MARRIAGE",'e':"ENIMIES",'s':"SIBLINGS"}
	k=0
	for i in first_name:
		if i  in second_name:
			first_name=first_name.replace(i,"",1)
			second_name=second_name.replace(i,"",1)
    
	s=len(first_name)+len(second_name)
	le=len(f)
	while(le!=1):
		first_name=s
		while(first_name):
			if(k<len(f)):
				first_name=first_name-1
				k=k+1
			else:
				k=1
				first_name=first_name-1
		f=f.replace(f[k-1],"")
		le=le-1
		k=k-1
	f=f
	for i,j in d.items():
		if(i==f):
			f="The relation between two names is:"+j
			return f

	'''text1 =text1.upper()
	text2 =text2.upper()
	combine = text1 +text2
	return combine'''

@app.route('/')
def home():
	return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
	first_name = request.form['first_name']
	#word = request.args.get('first_name')
	second_name= request.form['second_name']
	f = do_something(first_name,second_name)
	result = {"output": f}
	result = {str(key): value for key, value in result.items()}
	return jsonify(result=result)
if __name__ == '__main__':
	app.run(debug=True)






	''' name1=firstName.text;
  name2=secondName.text;
  name1 = name1.toLowerCase();
  name2 = name2.toLowerCase();
List<String> name1Split = name1.split(" ");
List<String> name2Split = name2.split(" ");
name1="";
name2="";
for(int i=0;i<name1Split.length;i++)
{
name1 = name1+name1Split[i];
}
for(int i=0;i<name2Split.length;i++)
{
name2 = name2+name2Split[i];
}
int length = name1.length+name2.length;
//boolean name_check[] = new boolean[name2.length];
var nameCheck = new List(name2.length);
for(int i=0;i<name2.length;i++)
{
nameCheck[i]=false;
}
for(int i=0;i<name1.length;i++)
{
for(int j=0;j<name2.length;j++)
{
if((nameCheck[j]==false) && (name1.contains(name1[i]) == name2.contains(name2[j])))
{
nameCheck[j]=true;
length = length-2;
break;
}
}
}
var flamesCheck = new List(name2.length);
for(int i=0;i<6;i++)
{
flamesCheck[i] = true;
}
int c = 6;
int k=1,deletedLetters=0;
int j;
for(j=0;j<=c;j++){
  if(k <= length)
  {
    if(j == c)
    {
      j=0;
    }
if(flamesCheck[j] == true)
{
  k = k+1;
}
}
if((k-1)==length)
{
  deletedLetters = deletedLetters+1;
  flamesCheck[j] = false;
  k = 1;
}
if(deletedLetters==6)
{
  
if(j==0)
{

}
else if(j==1)
{
  rel = "lovers";
}
else if(j==2)
{
rel = "AFFECTION";
}
else if(j==3)
{
rel = "MARRIAGE";
}
else if(j==4)
{
rel = "ENEMIES";
}
else if(j==5)
{
rel = "SIBLINGS";
}
break;
}
}'''




	'''
int i, j, k, l = 1, n, m, sc = 0, tc, rc = 0, fc = 5; 
    var c; 
    var f = "flames".split(""); 
    List<String> q= name1.split(" ");
    List<String> w= name2.split(" ");
    
     n = name1.length;
	   m = name2.length;
     tc = n + m; 
  
    for (i = 0; i < n; i++) { 
        c = name1[i]; 
        for (j = 0; j < m; j++) { 
            if (c == name2[j]) { 
                q[i] = -1;
                print(name1[i]);
                name2[j] = -1; 
                print(name2[i]);
                sc = sc + 2; 
                break; 
            } 
        } 
    } 
  
    rc = tc - sc; 
  
    for (i = 0;; i++) { 
        if (l == (rc)) { 
            for (k = i; f[k] != '\0'; k++) { 
                f[k] = f[k + 1]; 
            } 
            f[k + 1] = '\0'; 
            fc = fc - 1; 
            i = i - 1; 
            l = 0; 
        } 
        if (i == fc) { 
            i = -1; 
        } 
        if (fc == 0) { 
            break; 
        } 
        l++; 
    } 
  
   // Print the results 
    if (f[0] == 'e') 
           rel = "ENEMIES";
    else if (f[0] == 'f') 
          rel = "FRIENDS";
    else if (f[0] == 'm') 
           rel = "MARRIAGE";
    else if (f[0] == 'l') 
      rel = "LOVERS";
    else if (f[0] == 'a') 
           rel = "AFFECTION";
    else
        rel = "SIBLINGS";'''
    
