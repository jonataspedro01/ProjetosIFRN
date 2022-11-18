import * as React from 'react';
import { Text, View, StyleSheet, Button } from 'react-native';
import Constants from 'expo-constants';
import Teclado from './teclado'
import XButton from './XButton'

export default function App() {
   
  const [display, displaySet ]= React.useState(0)
  const [memoria, memoriaSet ]= React.useState(0)
   const [operacao, operacaoSet ]= React.useState("")

  function tecla(valor) {
    if(valor=="C"){
     displaySet(0)
     memoriaSet (0)
     operacaoSet ("")

    }else    if(valor=="="){
      if(operacao=="+"){
       displaySet(memoria + display)
      } else if (operacao=="-"){
       displaySet(memoria - display)
    }else    if(operacao=="X"){
      displaySet(memoria * display)
     }else    if(operacao=="/"){
     displaySet(memoria / display)
     }
    } else    if(valor=="+"){
   memoriaSet(display)
operacaoSet(valor)
displaySet(0)
    }else    if(valor=="-"){
memoriaSet(display)
operacaoSet(valor)
displaySet(0)
      }else    if(valor=="X"){ 
     memoriaSet(display)
     operacaoSet(valor)
     displaySet(0)
      }else    if(valor=="/"){
memoriaSet(display)
operacaoSet(valor)
displaySet(0)
      }else  {
       displaySet(display * 10 + valor)
      }

  }

 const size = 300;

  return (

    
    <View style={{
      width: 350,
      paddig: 5,
      borderRadius: 10,
      margin: 6,
      marginLeft: 5,
      marginRight: -28,
      marginTop: 40,
      backgroundColor: 'orange'
      }}>
 <Text  
 style={{
   fontSize: 20 , 
   textAlign: 'center' , 
   color: 'black',
   marginVertical: 0, }}>
    BRASIL RUMO AO HEXA!
    </Text>
      <Text 
     style={{fontSize: 30 }}>
    {memoria} {operacao}
    </Text>
     <Text 
     style={{
       fontSize: 90, 
       backgroundColor: '#DCDCDC', 
       textAlign: "right" , 
       marginRight:0.6,
       border: 'black',
      borderColor: 'black',
       }}>
     {display}
     </Text>
      <Teclado onKey={tecla} size={size-30}/>
    </View>
  ); 
}







