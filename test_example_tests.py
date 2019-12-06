class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_user_page_view(self):
        """
        Test that user page is inaccessible without login
        """
        target_url = url_for('user', user_id=1)
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_ticket_model(self):
        """
        Test number of records in Ticket table
        """

        # create test ticket
        ticket = Ticket(film_title="example", cinema="Other", cinema_other="Example",town="example", date="01/01/19", time="00:00", rating="10", review="This is an example ticket")

        # save ticket to database
        db.session.add(ticket)
        db.session.commit()

        self.assertEqual(Ticket.query.count(), 1)