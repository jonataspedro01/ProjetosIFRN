import * as React from 'react';
import { Text, View, StyleSheet, Button  } from 'react-native';
import Constants from 'expo-constants';

export default function XButton (props: IXButton)
{
  function tecla(key){
    props.onPress(key)
  }

  const size = (props.size ?? 50) -1 ;

  return (
    <View>
  <Text  
      style={{
    margin: 1 , 
    marginLeft: 5.5,
    marginHorizontal: 20,
    marginVertical: 11,
    borderRadius: 140, 
    backgroundColor: 'green',
    width: size,
    height: 90,
    fontSize: 70,
    textAlign: 'center',
    color: 'white',
    }} 
    onPress={() => tecla(1)}>
    {props.title}
    </Text> 
    </View>
 );
}

interface IXButton {
  title: string;
  onPress: (k) => void;
  size: number;
}