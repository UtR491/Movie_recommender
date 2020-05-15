import 'package:flutter/material.dart';

class BookDetail extends StatefulWidget {
  @override
  _BookDetailState createState() => _BookDetailState();
}

class _BookDetailState extends State<BookDetail> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[100],
        iconTheme: IconThemeData(
          color: Colors.black
        ),
        actions: <Widget>[
          
        ],
        title: Text(
            "BookName",
          style: TextStyle(
            fontFamily: "BalooChettan",
            fontWeight: FontWeight.bold,
            color: Colors.black
          ),
        ),
        centerTitle: true,
      ),
      body: Text(
          "ghughegehg",
        style: TextStyle(
          fontFamily: "BalooChettan",
        ),
      ),
    );
  }
}
