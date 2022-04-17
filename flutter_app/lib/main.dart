
import 'package:flutter/material.dart';
import 'package:trycycle3/Home.dart';
import 'package:trycycle3/videos.dart';
import 'package:trycycle3/settings.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fatfuck',
      theme: ThemeData(
        primarySwatch: Colors.red,
      ),
      initialRoute:'home',
      routes:{
        'home' : (context) => Home(title:'Testing 1'),
        'videos': (context) => Videos(),
        'settings':(context)=> Settings(),

      }
    );
  }
}

