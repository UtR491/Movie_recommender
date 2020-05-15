import 'package:flutter/material.dart';
import 'book_detail.dart';
import 'home.dart';

void main()
{
  runApp(
    MaterialApp(
      initialRoute: '/',
      routes: {
        '/':(context){
          return Home();
        },
        '/detail':(context){
          return BookDetail();
        }
      },
    ),
  );
}