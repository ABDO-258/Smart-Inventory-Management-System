import React from 'react';
import './Footer.css';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCity } from '@fortawesome/free-solid-svg-icons';
import { faFacebookF, faInstagram, faYoutube, faTwitter, faLinkedin } from '@fortawesome/free-brands-svg-icons';

function Footer() {
  return (
    <div className='footer-container'>
      <section className='social-media'>
        <div className='social-media-wrap'>
          <div className='footer-logo'>
            <Link to='/' className='social-logo'>
              Smart IMS
              <FontAwesomeIcon icon={faCity} />
            </Link>
          </div>
          <small className='website-rights'>Smart Inventory Management System © 2024</small>
          <div className='social-icons'>
            <Link
              className='social-icon-link facebook'
              to='/'
              target='_blank'
              aria-label='Facebook'
            >
              <FontAwesomeIcon icon={faFacebookF} />
            </Link>
            <Link
              className='social-icon-link instagram'
              to='/'
              target='_blank'
              aria-label='Instagram'
            >
              <FontAwesomeIcon icon={faInstagram} />
            </Link>
            <Link
              className='social-icon-link youtube'
              to='/'
              target='_blank'
              aria-label='Youtube'
            >
              <FontAwesomeIcon icon={faYoutube} />
            </Link>
            <Link
              className='social-icon-link twitter'
              to='/'
              target='_blank'
              aria-label='Twitter'
            >
              <FontAwesomeIcon icon={faTwitter} />
            </Link>
            <Link
              className='social-icon-link linkedin'
              to='/'
              target='_blank'
              aria-label='LinkedIn'
            >
              <FontAwesomeIcon icon={faLinkedin} />
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Footer;