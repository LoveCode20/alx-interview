#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const fetchCharacterNames = async () => {
  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request(filmUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          reject(new Error(`Failed to fetch film data: ${error || response.statusCode}`));
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characterUrls = filmResponse.characters;
    const characterPromises = characterUrls.map(url => 
      new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            reject(new Error(`Failed to fetch character data: ${error || response.statusCode}`));
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      })
    );

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error('Error:', error.message);
  }
};

fetchCharacterNames();

