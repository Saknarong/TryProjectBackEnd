import React, { Component } from 'react';
import { StyleSheet, Text, View, ScrollView, Image, ImageBackground, TouchableOpacity, FlatList, Button } from 'react-native';
import axios from 'axios';



export default class SelectPageFemale extends Component {

  state = {
    data: []
  }


  getShape = async () => {
    const resp = await axios.get('http://3.84.76.238:8000/womanShape/')
    console.log('shape is serving....')
    let data = resp.data.map(value => {
      return value
    })
    this.setState({ data })

  }
  componentDidMount = async () => {
    await this.getShape()
    console.log('serving done!');
  }

  render() {

    return (
      <ScrollView>

        <ImageBackground
          source={require('./android/app/img/bg.png')}
          style={styles.ImageBackgroundStyle}>
          <View>
            <Text style={styles.TextStyle}>Select Your Body Shape </Text>
          </View>
          <View style={styles.Container}>
            <View style={styles.Container}>
              {this.state.data.map((val, index) => (

                <View key={index}>
                  {console.log(val.shapePictureUrl)}
                  {val.shapePictureUrl && val.shapePictureUrl.length !== 0 ? (

                    <TouchableOpacity style={styles.shapeContainer}>

                      <Image style={styles.ImageStyle}
                        resizeMode='contain'
                        source={{ uri: `${val.shapePictureUrl}` }}

                      />
                      <View style={{justifyContent: 'center'}}>
                        <Text styles={styles.nameOfShapeStyle}>{val.shapeName}</Text>
                      </View>
                    </TouchableOpacity>

                  ) : (<Text>No image</Text>)}

                </View>


              ))}
            </View>


          </View>


        </ImageBackground>
      </ScrollView>

    );
  }
}

const styles = StyleSheet.create({
  ImageBackgroundStyle: {
    width: '100%',
    marginTop: 0,
    height: 5500
  },
  TextStyle: {
    fontSize: 20,
    textAlign: 'center',
    marginTop: 90,
    color: 'white',
    fontWeight: 'bold'
  },
  Container: {
    backgroundColor: 'white',
    borderRadius: 10,
    marginLeft: 10,
    marginRight: 10,
    marginBottom: 10,
    marginTop: 50,
    height: 5500,
    flex: 1
  },
  shapeContainer: {
    marginLeft: 10,
    marginRight: 10,
    width: '90%',
    marginTop: 10,

  },
  bottonClick: {
    width: 120,
    height: 300,
    backgroundColor: 'white',
    borderRadius: 10,
    borderWidth: 0.5,
    borderColor: '#E9E9E9',
    marginLeft: 20,
  },
  nameOfShape: {
    textAlign: 'center',
    marginBottom: 15,
    marginTop: 10,
    justifyContent: 'center'

  },
  nameOfShapeStyle: {
    color: 'gray',
    fontWeight: 'bold',
  },
  ImageStyle: {
    height: 300,
    width: '100%',
    justifyContent: 'center',
    borderColor: 'black',
    border: '1'

  },

});
