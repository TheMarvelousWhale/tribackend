import 'package:flutter/material.dart';
import 'package:trycycle3/sidedrawer.dart';
import 'package:trycycle3/tabs/Bottom/Camera.dart';
import 'package:trycycle3/tabs/Bottom/Gallery.dart';
import 'package:trycycle3/tabs/Bottom/threed.dart';


class Home extends StatefulWidget{
  const Home({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home>{
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
        length: 3,
        child:Scaffold(
      appBar: AppBar(
          title: Text(widget.title),
        bottom:TabBar(
          tabs:[
            Tab(
                text:'3D',
                   icon: Icon(Icons.home),
            ),
            Tab(
              text:'Gallery',
              icon: Icon(Icons.browse_gallery),
            ),
            Tab(
              text:'Camera',
              icon: Icon(Icons.camera),
            ),
          ],
        ),
      ),

      drawer:SideDrawer(),
      body: TabBarView(
        children:[
          threed(),
          Gallery(),
          Camera(),

        ],
      ),

      floatingActionButton: FloatingActionButton(
        tooltip:'Increment',
        child: Icon(Icons.camera),
        onPressed:(){}
      ),
    ),
    );
  }
}