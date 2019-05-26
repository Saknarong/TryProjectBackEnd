import React, { Component } from 'react';
import { StyleSheet, Text, View, ScrollView, Image, ImageBackground, TouchableOpacity, FlatList, Button } from 'react-native';
import axios from 'axios';



export default class ShowClothes extends Component {

  state = {
    data: []
  }


  getClothes = async () => {
    const resp = await axios.get('http://3.84.76.238:8000/clothesManagement/')
    console.log('clothes is serving....')
    let data = resp.data.map(value => {
      return value
    })
    this.setState({ data })

  }
  componentDidMount = async () => {
    await this.getClothes()
    console.log('serving done!');
  }

  render() {

    return (
      <ScrollView>
        <View style={{ backgroundColor: '#F5F5F5' }}>
          <View>
            <Text style={styles.header}>Clothes</Text>
          </View>
          {this.state.data.map((val, index) => (
            <View key={index}>
              {console.log(val.clothePictureUrl)}
              {val.clothePictureUrl && val.clothePictureUrl.length !== 0 ? (

                <TouchableOpacity style={styles.clothesContainer}>

                  <Image style={styles.ImageStyle}
                    resizeMode='contain'
                    source={{ uri: `${val.clothePictureUrl}` }}
                  />
                  <Text styles={styles.nameOfClothesStyle}>{val.clotheName }</Text>
                </TouchableOpacity>
              ) : (<Text>No image</Text>)}

            </View>
          ))}
        </View>

      </ScrollView>

    );
  }
}

const styles = StyleSheet.create({
  Container: {
    textAlign: 'center',
    backgroundColor: '#F5F5F5',
    height: 1500,
  },
  header: {
    fontSize: 20,
    color: '#949494',
    fontWeight: 'bold',
    padding: 15,
    textAlign: 'center',
    backgroundColor: '#F5F5F5'

  },
  clothesContainer: {
    marginLeft: 10,
    marginRight: 10,
    width: '95%',
    marginTop: 10,
    backgroundColor: '#FFFFFF',
  },
  nameOfClothesStyle: {
    color: 'gray',
    fontSize: 40,
    fontWeight: 'bold',
    textAlign: 'center',
    marginLeft:50,
  },
  ImageStyle: {
    height: 300,
    width: '100%',
    justifyContent: 'center',
    marginTop: 10
  },

});
