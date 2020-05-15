import 'package:bookrecommender/screens/home/book_card.dart';
import 'package:flutter/material.dart';

class Books extends StatefulWidget {
  @override
  _BooksState createState() => _BooksState();
}

class _BooksState extends State<Books> {
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: 2,
      itemBuilder: (context, index){
        return BookCard();
      },
    );
  }
}
