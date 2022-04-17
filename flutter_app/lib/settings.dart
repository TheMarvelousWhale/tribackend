import 'package:flutter/material.dart';
import 'package:trycycle3/sidedrawer.dart';

class Settings extends StatefulWidget{
  @override
  _SettingState createState() => _SettingState();
}

class _SettingState extends State<Settings>{
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
        title: Text('Settings',
        ),
      ),
    );
  }
}