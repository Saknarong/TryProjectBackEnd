import React from 'react';
import {
 StyleSheet,
 Text,
 View,
 TouchableOpacity,
 Image
} from 'react-native';


export default class App extends React.Component{


 render(){
   return(

     <View style={styles.Container}>
     <View style={styles.top}>
       <Text style={styles.header}>Select Your Genger</Text>
       </View>
       <View style={styles.styleButton}> 
       <TouchableOpacity style={styles.genderContainer}>
            <Image 
            source={require('./android/app/img/female.png')}
            style={styles.imageStyle}/>
        </TouchableOpacity>
        <TouchableOpacity style={styles.genderContainer}>
            <Image
            source={require('./android/app/img/male.png')}
            style={styles.imageStyle}/>
            </TouchableOpacity>
        </View>
        <View style={styles.bottonClick}>
        <TouchableOpacity style={styles.botton}>
          <Text style={styles.bottonText}>Next ></Text>
        </TouchableOpacity>
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
     alignItems:'center',
     marginBottom:30,
     marginTop:50
   },
   header:{
     fontSize: 23,
     padding:50,
     paddingLeft:40,
     paddingRight:40,
     color:'#949494',
   },
   bottonText:{
     fontSize:20,
     fontWeight:'500',
     color:'#8B8B8B',
     textAlign:'center'
  },
  bottonClick:{
    flex:1,
    justifyContent:'center',
    alignItems:'center',
    marginTop:40
   },
  botton:{
    width:200,
    backgroundColor:'#F9F9F9',
    borderRadius: 25,
    marginVertical:10,
    paddingVertical:12
    },
    imageStyle:{
       width:'100%',
       height:'100%',
       borderRadius: 10,    
   },
   styleButton:{
      flex:1,
      flexDirection: 'row',
      justifyContent: 'center',
   },
   genderContainer:{
    height:'110%',
    width:'40%',
    marginLeft:20,
    marginRight:20
    
   }
     



 });
