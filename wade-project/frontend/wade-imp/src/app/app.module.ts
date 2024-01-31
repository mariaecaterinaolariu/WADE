import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UploadService } from './features/upload/upload.service';
import { UploadComponent } from './features/upload/upload.component';
import { HttpClientModule } from '@angular/common/http';
import { PortraitsComponent } from './features/portraits/portraits.component';
import { PortraitsService } from './features/portraits/portraits.service';
import { Base64Pipe } from './shared/pipes/convert-base64.pipe';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import{ MatMenuModule } from '@angular/material/menu';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

@NgModule({
  declarations: [
    AppComponent,
    UploadComponent,
    PortraitsComponent,
    Base64Pipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatIconModule,
    MatButtonModule,
    MatInputModule, 
    MatFormFieldModule,
    MatMenuModule 
  ],
  providers: [
    UploadService,
    PortraitsService,
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
