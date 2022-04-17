import 'package:flutter/material.dart';
import 'package:flutter_cube/flutter_cube.dart';

class threed extends StatelessWidget {
  const threed({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Prototype1'),

    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override



  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override

  late Object jennie;
  void initState() {
    jennie=Object(fileName: "assets/jennie/jennie.obj");
    super.initState();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Cube(onSceneCreated: (Scene scene){
          scene.world.add(jennie);
          scene.camera.zoom=10;
        },

        ),
      ),// This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
