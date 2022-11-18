import * as React from 'react';
import { Text, View, StyleSheet, Button } from 'react-native';
import Constants from 'expo-constants';
import XButton from './XButton';

export default function Teclado (props: ITeclado){


function tecla(key) {
  props.onKey(key)
}

const size = props.size ?? 200;
  return (
    <View style={{
      width: 120,
      }}>
  

      <View style={{flexDirection: 'row'}}>
        <XButton title="1" onPress={() => tecla(1)} size={size/4}/> 
        <XButton title="2"onPress={() => tecla(2)} size={size/4}/>   
        <XButton  title="3"onPress={() => tecla(3)} size={size/4}/>
          <XButton  title="+"onPress={() => tecla("+")} size={size/4}/>
      </View> 
      <View style={{flexDirection: 'row'}}>
        <XButton title="4"onPress={() => tecla(4)} size={size/4}/>
        <XButton title="5"onPress={() => tecla(5)} size={size/4}/> 
        <XButton  title="6"onPress={() => tecla(6)} size={size/4}/>
          <XButton  title="-"onPress={() => tecla("-")} size={size/4}/>
      </View>
      <View style={{flexDirection: 'row' }}>  
        <XButton  title="7"onPress={() => tecla(7)} size={size/4}/>
        <XButton  title="8"onPress={() => tecla(8)} size={size/4}/>
        <XButton  title="9"onPress={() => tecla(9)} size={size/4}/>
          <XButton  title="*"onPress={() => tecla("X")} size={size/4}/>
      </View>
       <View style={{flexDirection: 'row'}}>  
        <XButton  title="C"onPress={() => tecla("C")} size={size/4}/>
        <XButton  title="0"onPress={() => tecla(0)} size={size/4}/>
        <XButton  title="="onPress={() => tecla("=")} size={size/4}/>
          <XButton  title="/"onPress={() => tecla("/")} size={size/4}/>
      </View>
    </View>
    );
}

interface ITeclado
{
   onKey: (Key) => void;
   size: Number;
}






