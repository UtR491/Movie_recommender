import 'package:bookrecommender/shared/loading.dart';
import 'package:flutter/material.dart';
import 'package:bookrecommender/services/auth.dart';

class SignIn extends StatefulWidget {

  final Function toggleView;
  SignIn({this.toggleView});

  @override
  _SignInState createState() => _SignInState();
}

class _SignInState extends State<SignIn> {

  final AuthService _auth = AuthService();
  final _formKey = GlobalKey<FormState>();
  bool loading = false;

  String email="", password="", error="";

  @override
  Widget build(BuildContext context) {
    if(loading) return Loading();
    else
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        actions: <Widget>[
          FlatButton.icon(
            splashColor: Colors.brown[200],
            highlightColor: Colors.brown[100],
            icon: Icon(Icons.person),
            label: Text(
              "REGISTER",
              style: TextStyle(
                color: Colors.black,
                fontFamily: "BalooChettan",
                fontWeight: FontWeight.bold
              ),
            ),
            onPressed: () {
              print("Pressed register button in Sign in screen");
              widget.toggleView();
              print("Called");
            },
          )
        ],
        backgroundColor: Colors.brown[100],
        title: Text(
          "SIGN IN",
          style: TextStyle(
              color: Colors.black,
              fontFamily: "BalooChettan",
              fontWeight: FontWeight.bold
          ),
        ),
        centerTitle: true,
        elevation: 20.0,
      ),
      body: SafeArea(
        child: Container(
          decoration: BoxDecoration(
              image: DecorationImage(
                image: AssetImage("assets/background.jpg"),
                fit: BoxFit.cover,
              )
          ),
          padding: EdgeInsets.symmetric(vertical: 20.0, horizontal: 50),
          child: Form(
            key: _formKey,
            child: Column(
              children: <Widget>[
                SizedBox(height: 113,),
              TextFormField(
                validator: (val) => val.isEmpty ? "Email field cannot be empty" : null,
                cursorColor: Colors.brown[400],
                decoration: InputDecoration(
                  fillColor: Colors.brown[100],
                  filled: true,
                  hintText: "Email",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(20.0),
                    borderSide: BorderSide(
                        color: Colors.brown[400],
                        width: 2.5
                    ),
                  ),
                ),
                onChanged: (val){
                  setState(() {
                    email = val;
                  });
              },
                ),
                SizedBox(height: 20,),
                TextFormField(
                  validator: (val) => val.length<=6 ? "Password must be at least 6 characters long" : null,
                  cursorColor: Colors.brown[400],
                  decoration: InputDecoration(
                    fillColor: Colors.brown[100],
                    filled: true,
                    hintText: "Password",
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(20.0),
                      borderSide: BorderSide(
                          color: Colors.brown[400],
                          width: 2.5
                      ),
                    ),
                  ),
                  obscureText: true,
                  onChanged: (val){
                    setState(() {
                      password = val;
                    });
                  },
                ),
                SizedBox(height: 40,),
                RaisedButton(
                  elevation: 20.0,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0),
                  ),
                  color: Colors.brown[400],
                  splashColor: Colors.brown[100],
                  child: Text(
                    "Sign In",
                    style: TextStyle(
                      fontSize: 20,
                      color: Colors.white,
                      fontFamily: "BalooChettan",
                        fontWeight: FontWeight.bold
                    ),
                  ),
                  onPressed: () async {
                    if(_formKey.currentState.validate()){
                      setState(() {
                        return loading = true;
                      });
                      dynamic result = await _auth.singInWithEmailAndPassword(email, password);
                      if(result == null){
                        setState(() {
                          loading = false;
                          error = "Incorrect Credentials";
                        });
                      }
                    }
                  },
                ),
                SizedBox(height: 10,),
                Text(
                  error,
                  style: TextStyle(
                      fontSize: 14.0,
                      fontFamily: "Baloo Chettan",
                      color: Colors.red
                  ),
                )
              ],
            ),
          ),
          ),
      ),
    );
  }
}
//
//FlatButton(
//shape: RoundedRectangleBorder(
//borderRadius: BorderRadius.circular(20)),
//color: Colors.orange[600],
//splashColor: Colors.orange[100],
//child: Text(
//"Sign in Anonymously",
//style: TextStyle(
//color: Colors.white,
//fontFamily: "BalooChettan",
//),
//),
//onPressed: () async {
//dynamic result = await _auth.signInAnon();
//if(result != null) {
//print("Signed in");
//print(result.uid);
//}
//else
//print("Not signed in $result");
//},
//),

