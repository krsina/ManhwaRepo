
import React from 'react';
import './styles.css';

const Card = ({ image, title, link, latestChapter }) => {
  return (
    <div className="card">
        <div className='card2'>
        <img className="card-image" src="https://img.asuracomics.com/unsafe/fit-in/720x936/https://asuratoon.com/wp-content/uploads/2023/11/RegressingwiththeKingsPowerCover01.png" alt={title} />
      <h3 className ="card-text">Regressing with the King’s Power</h3>
      <div className='card-chapter'>
      <a className ="card-chapter-button" href="https://asuratoon.com/0435219386-regressing-with-the-kings-power-chapter-17/">Chapter 17</a>
      <p className ="card-date">11/23/12</p>
      </div>
        </div>
    </div>
  );
};

export default Card;
