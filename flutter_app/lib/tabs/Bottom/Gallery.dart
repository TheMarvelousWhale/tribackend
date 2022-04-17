import 'package:flutter/material.dart';

class Gallery extends StatelessWidget{
  const Gallery({Key? key}):super(key:key);

  @override
  Widget build(BuildContext context){
    return Container(
      child: Center(
        child:
        Text('Tabs 2',
          style : TextStyle(fontSize:24),
        ),

      ),
    );
  }

}