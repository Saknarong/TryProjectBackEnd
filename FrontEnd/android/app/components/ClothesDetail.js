import React from 'react';
import {
 StyleSheet,
 Text,
 View,
 TouchableOpacity,
} from 'react-native';


export default class App extends React.Component{
 render(){
   return(

     <View style={styles.Container}>
     <View style={styles.top}>
       <Text style={styles.header}>Name Of Clothes</Text>
       </View>
        </View>
   );
 }
 }
 const styles = StyleSheet.create({
   Container: {
     flex:1,
     backgroundColor: '#F3F3F3'
   },
   top:{
     alignItems:'center'
   }
 });
