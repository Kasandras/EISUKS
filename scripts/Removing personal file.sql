Declare     @FistName   nvarchar(500)     = 'Автоматизация'
      ,           @LastName   nvarchar(500)     = 'Автоматизация'
      ,           @MiddleName nvarchar(500)    = 'Автоматизация'
      
      ,           @ID               UNIQUEIDENTIFIER  
      

      Declare DeletePersonalFile Cursor Local For
      select PersonalFiles.ID 
            from Applicant.PersonalFiles
            inner join Applicant.PersonalCardGeneralInformations 
                  on PersonalFiles.CardId = PersonalCardGeneralInformations.ID
                  and PersonalCardGeneralInformations.FirstName = @FistName
                  and PersonalCardGeneralInformations.LastName = @LastName
                  and PersonalCardGeneralInformations.MiddleName = @MiddleName
      Open DeletePersonalFile
      Fetch Next From DeletePersonalFile into @ID
      While @@FETCH_STATUS=0
      Begin
      
            exec [Applicant].[DeletePersonalFile]  @ID
            
            Fetch Next From DeletePersonalFile into @ID
            Continue

      end
      Close DeletePersonalFile
      Deallocate DeletePersonalFile 