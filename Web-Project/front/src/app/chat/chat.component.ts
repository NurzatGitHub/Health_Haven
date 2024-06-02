import { Component, OnInit } from '@angular/core';
import Pusher from 'pusher-js';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  username = 'username';
  message = '';
  messages: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    Pusher.logToConsole = true;

    const pusher = new Pusher('05a92c12726a780aacc0', {
      cluster: 'ap2'
    });

    const channel = pusher.subscribe('chat');
    channel.bind('message', (data: any) => {
      this.messages.push(data);
    });
  }

  submit(): void {
    this.http.post('http://localhost:8000/chat/messages', {
      username: this.username,
      message: this.message
    }).subscribe((response: any) => {
      // Assuming the server returns the new message
      this.messages.push(response);
      this.message = ''; // Clear the message input field
    });
  }

  onMessageChange(event: Event): void {
    const inputElement = event.target as HTMLInputElement;
    this.message = inputElement.value;
  }
}
