

import 'package:flutter/material.dart';

class SideDrawer extends StatelessWidget{
  const SideDrawer({Key ? key}) :super(key:key);
  @override
  Widget build(BuildContext context){
    return Container(
      child:SafeArea(
      child: Drawer(child:ListView(children:[
        UserAccountsDrawerHeader(
          accountName: Text('Poogie'),
          accountEmail: Text('SosigFatto@dev.cn'),
        currentAccountPicture: CircleAvatar(backgroundImage: AssetImage('assets/yua-mikami-11.jpeg'),),),
        ListTile(title:Text('Home'),
          leading:Icon(Icons.home),
        onTap:()=>Navigator.pushReplacementNamed(context, 'home',
        ),
        ),
        ListTile(title:Text('Video'),
          leading:Icon(Icons.camera),
          onTap:()=>Navigator.pushReplacementNamed(context, 'videos',
          ),
        ),
        ListTile(title:Text('Settings'),
          leading:Icon(Icons.browse_gallery),
          onTap:()=>Navigator.pushReplacementNamed(context, 'settings',
          ),
        ),
      ],
      ),
      ),
      ),
    );
  }
}