import 'package:bookrecommender/screens/home/book_detail.dart';
import 'package:bookrecommender/screens/home/books.dart';
import 'package:bookrecommender/screens/home/search.dart';
import 'package:bookrecommender/screens/home/settings.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';


void main() {
  runApp(Home());
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  int _currentIndex = 0;
  final List<Widget> _children = [Search(), Books(), Settings()];

  void onTabTapped(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          backgroundColor: Colors.grey[100],
          title: Text(
            "NEXT READ",
            style: TextStyle(
              color: Colors.black,
              fontFamily: "BalooChettan",
              fontWeight: FontWeight.bold
            ),
          ),
          centerTitle: true,
          elevation: 0.0,
        ),
        body: _children[_currentIndex],
        bottomNavigationBar: BottomNavigationBar(
          onTap: onTabTapped,
          currentIndex: _currentIndex,
          backgroundColor: Colors.grey[100],
          items: [
            BottomNavigationBarItem(
                icon: Icon(
                  Icons.search,
                ),
                title: Text(
                  "FIND",
                  style: TextStyle(
                      fontFamily: "BalooChettan"
                  ),
                )
            ),
            BottomNavigationBarItem(
              icon: Icon(
                Icons.book,
              ),
              title: Text(
                  "BOOKS",
                style: TextStyle(
                    fontFamily: "BalooChettan"
                ),
              )
            ),
            BottomNavigationBarItem(
                icon: Icon(
                  Icons.settings,
                ),
                title: Text(
                  "SETTINGS",
                  style: TextStyle(
                      fontFamily: "BalooChettan"
                  ),
                )
            ),
          ],
          selectedItemColor: Colors.orange[900],
          unselectedItemColor: Colors.black,
        ),
      ),
    );
  }
}
