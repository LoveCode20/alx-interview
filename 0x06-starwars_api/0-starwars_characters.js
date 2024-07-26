#!/usr/bin/env node

const request = require('request');

const movie = process.argv[2];
const StarPoint = `https://swapi-api.hbtn.io/api/films/${movie}`;
let person = [];
const names = [];

const requestCharacters = () => {
  return new Promise((resolve, reject) => {
    request(StarPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(`Error: ${err} | StatusCode: ${res ? res.statusCode : 'N/A'}`);
      } else {
        const jsonBody = JSON.parse(body);
        person = jsonBody.characters;
        resolve();
      }
    });
  });
};

const requestNames = () => {
  return new Promise((resolve, reject) => {
    if (person.length > 0) {
      let remaining = person.length;
      for (const p of person) {
        request(p, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            reject(`Error: ${err} | StatusCode: ${res ? res.statusCode : 'N/A'}`);
          } else {
            const jsonBody = JSON.parse(body);
            names.push(jsonBody.name);
            remaining -= 1;
            if (remaining === 0) {
              resolve();
            }
          }
        });
      }
    } else {
      reject('Error: Got no Characters for some reason');
    }
  });
};

const getCharNames = async () => {
  try {
    await requestCharacters();
    await requestNames();

    for (const n of names) {
      process.stdout.write(n + (n === names[names.length - 1] ? '' : '\n'));
    }
  } catch (err) {
    console.error('Failed to retrieve character names:', err);
  }
};

getCharNames();

