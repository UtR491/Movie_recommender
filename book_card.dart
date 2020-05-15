import 'dart:ui';

import 'package:bookrecommender/screens/home/book_detail.dart';
import 'package:flutter/material.dart';

class BookCard extends StatefulWidget {
  @override
  _BookCardState createState() => _BookCardState();
}

class _BookCardState extends State<BookCard> {

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 0.0,
      child: ListTile(
        onTap: () {
          try{
            Navigator.push(context, new MaterialPageRoute(
                builder: (context) =>
                new BookDetail()
            ));
          } catch(e) {
            print("ERROR- $e");
          }

        },
        title: Padding(
          padding: const EdgeInsets.fromLTRB(8.0, 2.0, 0.0, 0.0),
          child: Text(
            "The Hunger Games",
            style: TextStyle(
              fontFamily: "BalooChettan",
              fontSize: 20.0
            ),
          ),
        ),
        subtitle: Padding(
          padding: const EdgeInsets.fromLTRB(8.0, 1.0, 0.0, 0.0),
          child: Text(
            "Author",
            style: TextStyle(
              fontFamily: "BalooChettan",
            ),
          ),
        ),
        leading: ClipRRect(
          borderRadius: BorderRadius.circular(5.0),
          child: Image(
            image: AssetImage("assets/book.jpg"),
          ),
        ),
        trailing: Text("4.8"),
      ),
    );
  }
}
//Card(
//child: ListTile(
//onTap: () {
//updateTime(index);
//},
//title: Text(locations[index].location),
//leading: CircleAvatar(
//backgroundImage: AssetImage("assets/${locations[index].flag}"),
//),
//),
//);


//  Row(
//  crossAxisAlignment: CrossAxisAlignment.start,
//  children: <Widget>[
//  Padding(
//  padding: const EdgeInsets.all(8.0),
//  child: ClipRRect(
//  borderRadius: BorderRadius.circular(5.0),
//  child: Image(
//  image: AssetImage("assets/book.jpg"),
//  ),
//  ),
//  ),
//  ListTile(
//  title: Text(
//  "The Hunger Games",
//  style: TextStyle(
//  fontFamily: "BalooChettan"
//  ),
//  ),
//  )
//  ],
//  fdb

