import 'package:flutter/material.dart';

class Search extends StatefulWidget {
  @override
  _SearchState createState() => _SearchState();
}

class _SearchState extends State<Search> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          SizedBox(height: 60,),
          Text(
            """       Find books recommended\n            to you on the basis of\na book you have already finished.""",
            style: TextStyle(
              fontSize: 20.0,
              fontFamily: "BalooChettan"
            ),
          ),
          SizedBox(height: 60,),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              style: TextStyle(
                  fontFamily: "BalooChettan"
              ),
              decoration: InputDecoration(
                hintText: "A book you read...",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(10.0)
                ),
                focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(20.0),
                  borderSide: BorderSide(
                      color: Colors.orange[600],
                      width: 2.5
                  ),
                ),
              ),
            ),
          ),
          SizedBox(height: 60,),
          FlatButton(
            child: Text(
              "FIND ME BOOKS",
              style: TextStyle(
                fontFamily: "BalooChettan",
                fontWeight: FontWeight.bold,
              ),
            ),
            onPressed: () {},
            color: Colors.orange[600],
            splashColor: Colors.orange[100],
            textColor: Colors.white,
          )
        ],
      )
    );
  }
}
