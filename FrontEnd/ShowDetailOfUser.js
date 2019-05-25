import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Image
} from 'react-native';


export default class App extends React.Component {
  render() {
    return (
      <View style={styles.Container}>
        <View style={styles.header}>
          <TouchableOpacity style={styles.addButton}>
            <Image
              source={require('./android/app/img/add.png')}
              style={styles.addImageStyle} />
          </TouchableOpacity>
          <TouchableOpacity style={styles.historyButton}>
            <Image
              source={require('./android/app/img/history.png')}
              style={styles.historyImageStyle} />
          </TouchableOpacity>
        </View>
        <View style={styles.allStyle}>
        <View style={styles.whiteSpace}>
        </View>
        <View style={styles.shapeImage}>
        <Image
          source={require('./android/app/img/shape.png')}
          style={styles.shapeImageStyle} />
        </View>
        <View style={styles.allButton}>
        <TouchableOpacity style={styles.homeButton}>
            <Image
              source={require('./android/app/img/home.png')}
              style={styles.homeImageStyle} />
          </TouchableOpacity>
          <TouchableOpacity style={styles.saveButton}>
            <Image
              source={require('./android/app/img/save.png')}
              style={styles.saveImageStyle} />
          </TouchableOpacity>
          <Text style={styles.textSaveStyle}>save</Text>

          <Image
              source={require('./android/app/img/shapeshow.png')}
              style={styles.shapeStyle} />
            <Text style={styles.textShapeStyle}>save</Text>
            <Image
              source={require('./android/app/img/skincolor.png')}
              style={styles.skinColorStyle} />
            <Text style={styles.textSkinColorStyle}>skin color</Text>

            
        </View>
        </View>
      </View>

    );
  }
}
const styles = StyleSheet.create({
  Container: {
    flex: 1,
    backgroundColor: '#F3F3F3'
  },
  header: {
    backgroundColor: '#F5F5F5',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    padding:10
  },
  addButton: {
    marginTop: 4,
    marginRight: 160,
    width:'10%'
  },
  addImageStyle: {
    width: 25,
    height: 25
  },
  historyButton:{
    marginTop: 4,
    marginLeft: 160,
    width:'10%'
  },
  historyImageStyle:{
    width: 35,
    height: 35
  },
  allStyle:{
    flexDirection: 'row',
    width:'80%',
  },
  shapeImage: {
    width:'100%',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom:150
  },
  shapeImageStyle: {
    width:'140%',
    height:'140%',
  },
  allButton:{
    flexDirection: 'column'
  },
  homeButton:{
    marginTop: 20,
    marginLeft: 10
  },
  homeImageStyle:{
    width: 30,
    height: 30
  },
  saveButton:{
    marginTop: 10,
    marginLeft:10
  },
  saveImageStyle:{
    width: 30,
    height: 30
  },
  textSaveStyle:{
      fontSize:15,
      color:'#949494',
      marginLeft:10
  },
  shapeStyle:{
    marginTop: 350,
    width: 30,
    height: 30,
    marginLeft:5
  },
  textShapeStyle:{
    fontSize:10,
    color:'#949494',
    marginLeft:10
  },
  skinColorStyle:{
        width:40,
        height:40,
        marginTop: 10,
  },
  textSkinColorStyle:{
    fontSize:10,
    color:'#949494',
    marginRight:15
  },
  whiteSpace:{
    margin:10
  },
});
