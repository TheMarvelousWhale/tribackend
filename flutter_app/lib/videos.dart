import 'package:flutter/material.dart';
import 'package:trycycle3/sidedrawer.dart';

class Videos extends StatefulWidget{
  @override
  _VideosState createState() => _VideosState();
}

class _VideosState extends State<Videos>{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      drawer:SideDrawer(),
      body:Container(
        padding: EdgeInsets.all(16),
        child:Center(
          child: Text('Top Tabs'),

        ),
      ),
      appBar: AppBar(
        title: Text('fuck ni',
        ),
      ),
    );
  }
}