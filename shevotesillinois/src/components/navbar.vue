<template>
  <b-navbar type="light" variant="light">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">She Votes Illinois</a>
    </div>
    <ul class="nav navbar-nav">
      <b-nav-item href="/">Home</b-nav-item>
      <b-nav-item-dropdown text="What Can You Do?" right>
        <b-nav-item-dropdown text="Become Aware" right>
          <b-dropdown-item href="#">Why Your Vote Matters</b-dropdown-item>
          <b-dropdown-item href="#">How to Become a Registered Voter</b-dropdown-item>
          <b-dropdown-item href="#">Register to Vote</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item-dropdown text="Be Informed" right>
          <b-dropdown-item href="#">Making Power Accessible</b-dropdown-item>
          <b-dropdown-item href="#">Tools and Resources</b-dropdown-item>
          <b-dropdown-item href="#">Making Your Plan to Vote</b-dropdown-item>
          <b-dropdown-item href="#">Go Vote</b-dropdown-item>
            <b-nav-item-dropdown text="Guides" right>
              <b-dropdown-item href="#">Canvassing</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-nav-item-dropdown>
        <b-nav-item-dropdown text="Get Active" right>
          <b-nav-item-dropdown text="Build Your Community/Expand Your Power" right>
            <b-nav-item-dropdown text="How?" right>
              <b-dropdown-item href="#">Tell Your Friends</b-dropdown-item>
              <b-dropdown-item href="#">Volunteer</b-dropdown-item>
            </b-nav-item-dropdown>
            <b-dropdown-item href="#">Student Rep Program</b-dropdown-item>
            <b-nav-item-dropdown text="Current Initiatives" right>
              <b-dropdown-item href="#">Water For All Ordinance</b-dropdown-item>
              <b-dropdown-item href="#">UN CEDAW</b-dropdown-item>
              <b-dropdown-item href="#">Legislation</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-nav-item-dropdown>
          <b-dropdown-item href="#">Tools and Resources</b-dropdown-item>
          <b-dropdown-item href="#">Making Your Plan to Vote</b-dropdown-item>
          <b-dropdown-item href="#">Go Vote</b-dropdown-item>
            <b-nav-item-dropdown text="Guides" right>
              <b-dropdown-item href="#">Canvassing</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-nav-item-dropdown>

      </b-nav-item-dropdown>

      <b-nav-item-dropdown text="About Us" right>
        <b-dropdown-item href="#">Mission History</b-dropdown-item>
        <b-dropdown-item href="#">Board of Directors</b-dropdown-item>
        <b-dropdown-item href="#">Advisory Council</b-dropdown-item>
        <b-dropdown-item href="#">Volunteer Consultants</b-dropdown-item>
          <b-nav-item-dropdown text="Our Impact" right>
            <b-dropdown-item href="#">Work We've Done to Date</b-dropdown-item>
            <b-dropdown-item href="#">Legislation Passed</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown text="News" right>
            <b-dropdown-item href="#">Articles & Features</b-dropdown-item>
            <b-dropdown-item href="#">SVI Newsletters</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-dropdown-item href="/legrecap">Legislation Recap</b-dropdown-item>
          <b-dropdown-item href="#">Testimonials</b-dropdown-item>
          <b-dropdown-item href="#">Photos</b-dropdown-item>
          <b-dropdown-item href="#">Videos</b-dropdown-item>
      </b-nav-item-dropdown>

      <b-nav-item href="/blog">Our Blog</b-nav-item>


      <b-nav-item-dropdown text="Let's Connect" right>
        <b-dropdown-item href="#">Events</b-dropdown-item>
        <b-dropdown-item href="#">Partnerships</b-dropdown-item>
        <b-dropdown-item href="#">Contact Us Form</b-dropdown-item>
        <b-dropdown-item href="#">Join Our Mailing List</b-dropdown-item>
        <b-dropdown-item href="#">Follow us on FB, Twitter, Instagram,
        Snapchat and YouTube</b-dropdown-item>
        <b-dropdown-item href="#">Mailing address & Phone Number</b-dropdown-item>
      </b-nav-item-dropdown>

      <b-nav-item href="#">DONATE</b-nav-item>
    </ul>
  </b-navbar>
</template>
