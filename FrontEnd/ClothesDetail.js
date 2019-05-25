import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Image,
  Button,
  onPressLearnMore,
  onPress,
  ScrollView
} from 'react-native';


export default class App extends React.Component {
  render() {
    return (
      <View style={styles.Container}>
        <View style={styles.header}>
          <TouchableOpacity style={styles.backButton}>
            <Image
              source={require('./android/app/img/back.png')}
              style={styles.backImageStyle} />
          </TouchableOpacity>
          <Text style={styles.headerText}>Name Of Clothes</Text>
        </View>
        <Image style={styles.clothesImage}
          source={require('./android/app/img/clothes1.png')}
          style={styles.clothesImageStyle} />
        <Text style={styles.nameOfClothesStyle}>Name Of Clothes</Text>
        <Text style={styles.textStyle}>Select Color : </Text>
        <View style={styles.selectStyle}>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        </View>
        <Text style={styles.textStyle}>Select Pattern : </Text>
        <View style={styles.selectStyle}>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        <TouchableOpacity style={styles.select}>
        </TouchableOpacity>
        </View>
        <TouchableOpacity style={styles.nextButton}>
            <Image
              source={require('./android/app/img/nextbutton.png')}
              style={styles.nextImageStyle} />
          </TouchableOpacity>
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
    flexDirection: 'row'

  },
  headerText: {
    color: '#949494',
    fontSize: 23,
    padding: 10,
    textAlign: 'center',
    marginRight: 70,
    marginLeft: 20

  },
  backButton: {
    marginTop: 5,
    marginRight: 50
  },
  backImageStyle: {
    width: 20,
    height: 20
  },
  clothesImage: {
    width: '100%'
  },
  clothesImageStyle: {
    width: '100%',
    height: '50%'
  },
  nameOfClothesStyle: {
    color: '#949494',
    fontSize: 23,
    textAlign: 'center',
    marginTop: 10,
  },
  selectStyle: {
    flexDirection: 'row',
    marginLeft:35
  },
  select:{
    backgroundColor: '#E5ACA0',
    borderRadius: 50,
    width:40,
    height:40,
    marginLeft:15
  },
  textStyle: {
    marginLeft: 30,
    marginTop:5,
    marginBottom:5,
    fontSize: 20,
    color: '#949494'
  },
  nextButton:{
    width:200,
    height:90,
    alignItems:'center',
    marginTop:15,
    marginRight:100,
    marginLeft:100
  },
  nextImageStyle:{
    width:'100%',

  }

});
