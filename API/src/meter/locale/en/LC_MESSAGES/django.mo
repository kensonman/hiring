��    %      D  5   l      @     A     Q     _     r     �     �     �     �     �     �          0     N     \  !   u     �     �     �  '   �     	      !     B     W     u     �     �  "   �     �  !        $  #   ?     c     w     �     �     �  B  �  	               !   &     H     M     l  E   o  	   �  %   �     �  Z   �     G	     O	  X   [	     �	     �	     �	  M   �	  
   7
  I   B
     �
  ?   �
  	   �
  !   �
     �
  +        8  �   D     �  �   �     y          �     �     �                                                                         "         #          %                              $                    	   
      !                            meter.Histories meter.History meter.History.data meter.History.data.helptext meter.History.date meter.History.date.helptext meter.History.id meter.History.id.helptext meter.History.ipaddr meter.History.ipaddr.helptext meter.History.stored meter.History.stored.helptext meter.Reading meter.Reading.customerId meter.Reading.customerId.helptext meter.Reading.id meter.Reading.id.helptext meter.Reading.meterPointNumber meter.Reading.meterPointNumber.helptext meter.Reading.meterType meter.Reading.meterType.helptext meter.Reading.parent meter.Reading.parent.helptext meter.Reading.readDate meter.Reading.readDate.helptext meter.Reading.readingType meter.Reading.readingType.helptext meter.Reading.registerId meter.Reading.registerId.helptext meter.Reading.serialNumber meter.Reading.serialNumber.helptext meter.Reading.value meter.Reading.value.helptext meter.Readings meter.types.electric meter.types.gas Project-Id-Version: PACKAGE VERSION
Report-Msgid-Bugs-To: 
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language-Team: LANGUAGE <LL@li.org>
Language: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
 Histories History Raw-Data The raw-data that user submitted. Date The date of the user submitted ID The primary key of the history. It is also used as idempotency-check. IPAddress The IPAddress that user are submitted Target The target data that the user physical stored. If the data was delete, it will set to None Reading Customer ID The customer id is a unique identifier for a customer, it must always be globally unique ID The primary key of the reading Meter Point Number The meter point number. This can be used to uniquely identify a supply point. Meter Type The type of the meter readering. It can be Electric (MPAN) or GAS (MPRN). Parent Used to identify this reading is submitted with another reading Read Date The read date that user provided. Reading Type In example, it can be 'ANYTIME' or 'NIGHT'. Register ID The Register ID is the serial number on the register for that particular register. It can be used to uniquely identify a register, but not an energy supply. Serial Number Serial Number is the meter serial number is used to identify a meter, this number should be unique, however uniqueness cannot be assured. Value The phical value Readings Electric GAS 